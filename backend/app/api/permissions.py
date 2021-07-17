from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class BaseAccessPermission(IsAuthenticated):
    message = 'Method not allowed'


class StudentAccessPermission(BaseAccessPermission):

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return request.user.role == User.STUDENT


class TeacherAccessPermission(BaseAccessPermission):

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return request.user.role == User.TEACHER


class PrincipalAccessPermission(BaseAccessPermission):

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        return request.user.role == User.PRINCIPAL


class PTAccessPermission(BaseAccessPermission):
    """ Principal or Teacher access permission """
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        role = request.user.role
        return role == User.PRINCIPAL or role == User.TEACHER


class PTSAccessPermission(BaseAccessPermission):
    """ Principal or Teacher or Student access permission """
    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False
        role = request.user.role
        return role == User.PRINCIPAL or role == User.TEACHER or role == User.STUDENT
