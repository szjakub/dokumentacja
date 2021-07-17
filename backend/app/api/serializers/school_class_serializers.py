from rest_framework import serializers
from school.models import School, SchoolClass, Principal
from api.validators import school_class_label_validator
from api.serializers.read_only_serializers import StudentReadOnlySerializer


class SchoolClassSerializer(serializers.ModelSerializer):
    class_students = StudentReadOnlySerializer(many=True, read_only=True)

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

