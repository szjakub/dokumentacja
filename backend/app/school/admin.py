from django.contrib import admin
from school.models import (
    School, SchoolClass, Student, Subject
)
from .forms import SchoolForm, SubjectForm


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    form = SchoolForm
    list_display = ('pk', 'school_name', 'school_address', 'verified')


@admin.register(SchoolClass)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('pk', 'school', 'yearbook', 'class_label')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'school', 'school_class', 'user')

    @admin.display(empty_value='???')
    def first_name(self, obj):
        return obj.user.first_name

    @admin.display(empty_value='???')
    def last_name(self, obj):
        return obj.user.last_name


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    form = SubjectForm
    list_display = ('id', 'subject_name', 'school')
