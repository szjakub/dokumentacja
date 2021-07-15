from rest_framework import serializers
from django.contrib.auth import get_user_model

from school.models import School, SchoolClass, Student, Principal
from users.utils import username_generator, password_generator
from mail.tasks import student_created_email

from api.validators import school_class_label_validator
from api.serializers.user_serializers import CyprusUserSerializer
from api.serializers.school_class_serializers import SchoolClassReadOnlySerializer

User = get_user_model()


class StudentReadOnlySerializer(serializers.ModelSerializer):
    school_class = SchoolClassReadOnlySerializer()
    user = CyprusUserSerializer()

    class Meta:
        model = Student
        fields = ['pk', 'school_class', 'user']

    def to_representation(self, obj):
        representation = super().to_representation(obj)
        school_class_representation = representation.pop('school_class')
        user_representation = representation.pop('user')
        for key in school_class_representation:
            representation[key] = school_class_representation[key]
        for key in user_representation:
            representation[key] = user_representation[key]
        return representation

    def to_internal_value(self, data):
        school_class_internal, user_internal = {}, {}
        for key in SchoolClassReadOnlySerializer.Meta.fields:
            if key in data:
                school_class_internal[key] = data.pop(key)
        for key in CyprusUserSerializer.Meta.fields:
            if key in data:
                user_internal[key] = data.pop(key)
        internal = super().to_internal_value(data)
        internal['school_class'] = school_class_internal
        internal['user'] = user_internal
        return internal


class StudentSerializer(serializers.ModelSerializer):
    user = CyprusUserSerializer()
    yearbook = serializers.IntegerField()
    class_label = serializers.CharField()

    class Meta:
        model = Student
        fields = ['user', 'yearbook', 'class_label']

    def validate_class_label(self, data):
        return school_class_label_validator(data)

    def create(self, validated_data):
        request = self.context.get('request')
        principal = Principal.objects.get(user=request.user)
        school = School.objects.get(school_principal=principal)
        try:
            school_class = SchoolClass.objects.get(
                yearbook=validated_data.pop('yearbook'),
                class_label=validated_data.pop('class_label'),
                school=school)
        except SchoolClass.DoesNotExist:
            raise serializers.ValidationError(
                'school_class with such yearbook and class_label does not exists')

        user_data = validated_data.pop('user')
        username = username_generator(user_data['first_name'], user_data['last_name'])
        password = password_generator()
        user = User.objects.create(username=username, **user_data)
        user.set_password(password)
        user.save()
        student = Student.objects.create(school=school, user=user, school_class=school_class)
        student.save()
        student_created_email.delay(
            to=user.email,
            first_name=user.first_name, last_name=user.last_name,
            school_name=school.school_name, school_address=school.school_address)
        return student
