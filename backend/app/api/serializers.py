from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from school.models import School

from project import settings


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['username', 'password']


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ['principal_email', 'school_name', 'school_address']
