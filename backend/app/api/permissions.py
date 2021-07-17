from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseAccessPermission(permissions.BasePermission):
    message = 'Method not allowed'


class StudentAccessPermission(BaseAccessPermission):

    def has_permission(self, request, view):
        return request.user.role == User.STUDENT


class TeacherAccessPermission(BaseAccessPermission):

    def has_permission(self, request, view):
        return request.user.role == User.TEACHER


class PrincipalAccessPermission(BaseAccessPermission):

    def has_permission(self, request, view):
        return request.user.role == User.PRINCIPAL
