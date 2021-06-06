from rest_framework import serializers
from django.contrib.auth.models import User
from users import models as user_models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_models.Student
        fields = '__all__'
