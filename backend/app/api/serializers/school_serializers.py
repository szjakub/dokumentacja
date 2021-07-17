import logging

from rest_framework import serializers
from django.contrib.auth import get_user_model

from school.models import School, Principal
from users.utils import username_generator, password_generator
from mail.tasks import school_request_email

from api.serializers.user_serializers import CyprusUserSerializer

logger = logging.getLogger(__name__)

User = get_user_model()


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
