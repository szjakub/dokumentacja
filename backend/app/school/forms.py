from django import forms
from .models import School, Student, Subject


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('verified', 'school_name', 'school_address')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('school', 'school_class')


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('id', 'subject_name', 'school')


