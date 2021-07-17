from rest_framework import serializers
from django.contrib.auth import get_user_model

from school.models import Student, SchoolClass
from api.serializers.user_serializers import CyprusUserSerializer

User = get_user_model()


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
