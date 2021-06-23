from rest_framework import serializers
from django.contrib.auth import get_user_model

from school.models import School, Class, Student, Teacher, Principal
from users.utils import username_generator, password_generator
from mail.tasks import school_request_email

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
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ['id', 'yearbook', 'class_label', 'students']

    def create(self, validated_data):
        request = self.context.get('request')

        school = School.objects.get(principal=request.user)
        new_class = Class.objects.create(
            school=school,
            yearbook=validated_data['yearbook'],
            class_label=validated_data['class_label']
        )
        new_class.save()
        return new_class


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
