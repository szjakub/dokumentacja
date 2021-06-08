from rest_framework import serializers
from django.contrib.auth.models import User
from school import models as school_models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']


class PrincipalSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = school_models.School
        fields = ['user', 'school_name', 'school_address']
