from django.contrib import admin
from school.models import (
    School, Class
)
from .forms import SchoolForm


class SchoolAdmin(admin.ModelAdmin):
    form = SchoolForm


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    fields = ('school', 'yearbook', 'class_label')


admin.site.register(School, SchoolAdmin)
