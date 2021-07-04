import logging

from rest_framework import serializers
from django.contrib.auth import get_user_model

from school.models import School, SchoolClass, Student, Teacher, Principal
from users.utils import username_generator, password_generator
from mail.tasks import school_request_email

logger = logging.getLogger(__name__)

User = get_user_model()


class CyprusUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['school_name', 'school_address']


class SchoolRequestSerializer(serializers.ModelSerializer):
    user = CyprusUserSerializer()
    school = SchoolSerializer()

    class Meta:
        model = Principal
        fields = ['user', 'school']

    def validate(self, data):
        data['user']['role'] = User.PRINCIPAL
        return data

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        school_data = validated_data.pop('school')
        username = username_generator(user_data['first_name'], user_data['last_name'])
        user = User.objects.create(username=username, **user_data)
        user.set_password(password_generator())
        user.save()
        school = School.objects.create(**school_data)
        school.save()
        principal = Principal.objects.create(user=user, school=school)
        school_request_email.delay(
            to=user.email,
            first_name=user.first_name, last_name=user.last_name,
            school_name=school.school_name, school_address=school.school_address)
        return principal


class ClassSerializer(serializers.ModelSerializer):
    class_students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = SchoolClass
        fields = ['id', 'yearbook', 'class_label', 'class_students']

    def validate_class_label(self, data):
        if not data.isalpha():
            raise serializers.ValidationError('class_label must be letter from alphabet')
        return data.upper()

    def validate(self, data):
        request = self.context.get('request')
        principal = Principal.objects.get(user=request.user)
        school = School.objects.get(school_principal=principal)
        try:
            SchoolClass.objects.get(
                school=school,
                yearbook=data['yearbook'],
                class_label=data['class_label']
            )
        except SchoolClass.DoesNotExist:
            return data
        raise serializers.ValidationError(
            'school_class with such yearbook and class_label already exists')

    def create(self, validated_data):
        request = self.context.get('request')
        principal = Principal.objects.get(user=request.user)
        school = School.objects.get(school_principal=principal)
        new_class = SchoolClass.objects.create(
            school=school,
            yearbook=validated_data['yearbook'],
            class_label=validated_data['class_label']
        )
        new_class.save()
        return new_class


class StudentReadOnlySerializer(serializers.Serializer):
    first_name = serializers.ReadOnlyField()
    last_name = serializers.CharField()
    yearbook = serializers.IntegerField()
    class_label = serializers.CharField()


class StudentSerializer(serializers.ModelSerializer):
    user = CyprusUserSerializer()
    yearbook = serializers.ModelField(model_field=SchoolClass()._meta.get_field('yearbook'))
    class_label = serializers.ModelField(model_field=SchoolClass()._meta.get_field('class_label'))

    class Meta:
        model = Student
        fields = ['user', 'yearbook', 'class_label']

    def validate_class_label(self, data):
        if not data.isalpha():
            raise serializers.ValidationError('class_label must be letter from alphabet')
        return data.upper()

    def create(self, validated_data):
        request = self.context.get('request')
        principal = Principal.objects.get(user=request.user)
        school = School.objects.get(school_principal=principal)

