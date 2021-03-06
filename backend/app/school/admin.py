from django.contrib import admin
from school.models import (
    School, SchoolClass, Student
)
from .forms import SchoolForm


class SchoolAdmin(admin.ModelAdmin):
    form = SchoolForm


@admin.register(SchoolClass)
class ClassAdmin(admin.ModelAdmin):
    fields = ('school', 'yearbook', 'class_label')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('school', 'school_class')


admin.site.register(School, SchoolAdmin)
