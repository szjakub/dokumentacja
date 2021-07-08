import logging

from rest_framework import serializers
from django.contrib.auth import get_user_model

from school.models import School, SchoolClass, Student, Teacher, Principal, Subject, Lesson
from users.utils import username_generator, password_generator
from mail.tasks import school_request_email, student_created_email

from .validators import school_class_label_validator

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
        return school_class_label_validator(data)

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


class SchoolClassReadOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolClass
        fields = ['pk', 'yearbook', 'class_label']


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


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
