from rest_framework import serializers
from django.contrib.auth import get_user_model

from school.models import School, SchoolClass, Student, Principal
from users.utils import username_generator, password_generator
from mail.tasks import student_created_email


User = get_user_model()


class StudentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    yearbook = serializers.IntegerField()
    class_label = serializers.CharField()

    def validate(self, attrs):
        # validate user
        user_data = {
            'email': attrs['email'],
            'first_name': attrs['first_name'],
            'last_name': attrs['last_name']
        }
        user_exist = User.objects.filter(**user_data).exists()
        if user_exist:
            raise serializers.ValidationError('User already exist')

        # validate school_class
        request = self.context.get('request')
        principal = Principal.objects.get(user=request.user)
        school = School.objects.get(school_principal=principal)
        school_class_data = {
            'yearbook': attrs['yearbook'],
            'class_label': attrs['class_label'],
            'school': school
        }

        school_class_exist = SchoolClass.objects.filter(**school_class_data).exists()
        if not school_class_exist:
            raise serializers.ValidationError(
                'school_class with such yearbook and class_label does not exists')
        return attrs

    def create(self, validated_data):
        return_data = validated_data.copy()
        # get school class
        request = self.context.get('request')
        principal = Principal.objects.get(user=request.user)
        school = School.objects.get(school_principal=principal)
        school_class = SchoolClass.objects.get(
            yearbook=validated_data.pop('yearbook'),
            class_label=validated_data.pop('class_label'),
            school=school
        )

        # create user
        username = username_generator(validated_data['first_name'], validated_data['last_name'])
        password = password_generator()
        user = User.objects.create(username=username, **validated_data)
        user.set_password(password)
        user.save()

        # create student role
        student = Student.objects.create(school=school, user=user, school_class=school_class)
        student.save()

        # send email with credentials
        student_created_email.delay(
            to=user.email,
            first_name=user.first_name, last_name=user.last_name,
            school_name=school.school_name, school_address=school.school_address)

        return return_data

    def update(self, instance, validated_data):
        raise serializers.ValidationError('Not implemented')
