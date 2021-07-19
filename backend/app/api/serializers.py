from django.contrib.auth import get_user_model
from rest_framework import serializers
from api.validators import school_class_label_validator
from users.utils import username_generator, password_generator
from mail.tasks import student_created_email, school_request_email
from school.models import School, SchoolClass, Student, Principal, Subject, Lesson

User = get_user_model()


class CyprusUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class SchoolModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['school_name', 'school_address']


class SchoolClassModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolClass
        fields = ['pk', 'yearbook', 'class_label']


class StudentReadOnlySerializer(serializers.ModelSerializer):
    school_class = SchoolClassModelSerializer()
    user = CyprusUserModelSerializer()

    class Meta:
        model = Student
        fields = ['pk', 'school_class', 'user']


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
            'school_class with such yearbook and class_label already exist')

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


class SchoolRequestSerializer(serializers.ModelSerializer):
    user = CyprusUserModelSerializer()
    school = SchoolModelSerializer()

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
                'school_class with such yearbook and class_label does not exist')
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
            to=user.email, username=username, password=password,
            first_name=user.first_name, last_name=user.last_name,
            school_name=school.school_name, school_address=school.school_address
        )

        return return_data

    def update(self, instance, validated_data):
        raise serializers.ValidationError('Not implemented')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['pk', 'subject_name']

    def create(self, validated_data):
        request = self.context.get('request')
        principal = Principal.objects.get(user=request.user)
        school = School.objects.get(school_principal=principal)
        subject, created = Subject.objects.get_or_create(school=school, **validated_data)
        if not created:
            raise serializers.ValidationError('Subject with such name already exist')
        return subject


class LessonReadOnlySerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    school_class = SchoolClassModelSerializer()

    class Meta:
        model = Lesson
        fields = ['pk', 'subject', 'school_class', 'day', 'start_time', 'duration']


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['pk', 'subject', 'school_class', 'day', 'start_time', 'duration']

    def create(self, validated_data):
        request = self.context.get('request')
        principal = Principal.objects.get(user=request.user)
        school = School.objects.get(school_principal=principal)

        subject_queryset = Subject.objects.filter(school=school)
        school_class_queryset = Subject.objects.filter(school=school)

        try:
            subject = subject_queryset.objects.get(id=validated_data.pop('subject'))
            school_class = school_class_queryset.objects.get(id=validated_data.pop('school_class'))
        except Exception as e:
            raise serializers.ValidationError(repr(e))

        lesson = Lesson.objects.create(
            school=school, subject=subject, school_class=school_class, **validated_data)
        return lesson
