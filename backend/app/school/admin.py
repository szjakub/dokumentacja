from django.contrib import admin
from school.models import (
    School, Class, Teacher, Student
)
from .forms import SchoolCreationForm, SchoolChangeForm


class SchoolAdmin(admin.ModelAdmin):
    form = SchoolChangeForm
    add_form = SchoolCreationForm



@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    fields = ('school', 'yearbook', 'class_label')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = ('user', 'first_name', 'last_name', 'school')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('user', 'first_name', 'last_name', 'school_class')


admin.site.register(School, SchoolAdmin)
