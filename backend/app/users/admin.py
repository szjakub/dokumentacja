from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import CustomUser

from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('login', 'role', 'date_joined', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'role')
    fieldsets = (
        (None, {'fields': ('login', 'password')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'password1', 'password2', 'role', 'date_joined', ),
        }),
    )

    search_fields = ('login', 'role', 'date_joined')
    ordering = ('date_joined',)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
