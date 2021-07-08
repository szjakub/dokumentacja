from django.contrib import admin
from school.models import (
    School, SchoolClass
)
from .forms import SchoolForm


class SchoolAdmin(admin.ModelAdmin):
    form = SchoolForm


@admin.register(SchoolClass)
class ClassAdmin(admin.ModelAdmin):
    fields = ('school', 'yearbook', 'class_label')


admin.site.register(School, SchoolAdmin)
