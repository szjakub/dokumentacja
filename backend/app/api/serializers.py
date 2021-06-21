from rest_framework import serializers
from django.contrib.auth import get_user_model

from school.models import School, Class, Student
from users.utils import username_generator, password_generator
from mail.tasks import school_request_email

User = get_user_model()


class CyprusUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class SchoolRequestSerializer(serializers.ModelSerializer):
    principal = CyprusUserSerializer()

    class Meta:
        model = School
        fields = ['principal', 'school_name', 'school_address']

    def validate(self, data):
        data['principal']['role'] = User.PRINCIPAL
        return data

    def create(self, validated_data):
        principal_data = validated_data.pop('principal')
        username = username_generator(principal_data['first_name'], principal_data['last_name'])
        principal = User.objects.create(username=username, **principal_data)
        principal.set_password(password_generator())
        school = School.objects.create(principal=principal, **validated_data)
        school_request_email.delay(
            to=principal.email,
            first_name=principal.first_name, last_name=principal.last_name,
            school_name=school.school_name, school_address=school.school_address
        )
        return school


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
        fields = ['id', 'school_class']
