from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseAccessPermission(permissions.BasePermission):
    message = 'Method not allowed'

    def has_permission(self, request, view):
        if User.is_staff:
            return True
        return False


class StudentAccessPermission(BaseAccessPermission):

    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return True
        return request.user.role == User.STUDENT


class TeacherAccessPermission(BaseAccessPermission):

    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return True
        return request.user.role == User.TEACHER


class PrincipalAccessPermission(BaseAccessPermission):

    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return True
        return request.user.role == User.PRINCIPAL
