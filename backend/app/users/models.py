from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager


class CyprusUser(AbstractBaseUser, PermissionsMixin):
    PRINCIPAL = 'p'
    TEACHER = 't'
    STUDENT = 's'
    ROLE_CHOICES = (
        (PRINCIPAL, 'principal'),
        (TEACHER, 'teacher'),
        (STUDENT, 'student')
    )
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    username = models.CharField(
        'username', max_length=150, unique=True, validators=[UnicodeUsernameValidator],
    )
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.get_username()
