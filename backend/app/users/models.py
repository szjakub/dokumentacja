from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('p', 'principal'),
        ('t', 'teacher'),
        ('s', 'student')
    )

    login = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.login
