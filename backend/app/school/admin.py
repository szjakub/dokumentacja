from django.contrib import admin
from school.models import (
    School, Class, Teacher, Student
)


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    fields = ('principal', 'name', 'address')


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    fields = ('school', 'yearbook', 'class_label')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = ('user', 'first_name', 'last_name', 'school')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('user', 'first_name', 'last_name', 'school_class')

