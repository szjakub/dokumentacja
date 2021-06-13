from project import settings
from django.db import models

from .tasks import send_user_email
from .utils import username_generator, password_generator


class School(models.Model):
    principal = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    principal_email = models.EmailField(max_length=50, unique=True)
    school_name = models.CharField(max_length=100)
    school_address = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if self.verified:
            username = username_generator(str(self.principal_email))
            password = password_generator(username)
            user, created = settings.AUTH_USER_MODEL.objects.get_or_create(
                username=username, password=password, email=self.principal_email)
            if created:
                user.save()
                self.principal = user
                send_user_email.delay(username, password)
        super().save(*args, **kwargs)


class Class(models.Model):
    school = models.ForeignKey(School, related_name='classes', on_delete=models.CASCADE)
    yearbook = models.SmallIntegerField()
    class_label = models.CharField(max_length=2)

    objects = models.Manager()

    def __str__(self):
        return f'{self.yearbook}{self.class_label} in {self.school.name}'

    class Meta:
        verbose_name_plural = 'class'


class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school_class = models.ForeignKey(Class, related_name='students', on_delete=models.CASCADE)

    objects = models.Manager()


class Teacher(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school = models.ForeignKey(School, related_name='teachers', on_delete=models.CASCADE)

    objects = models.Manager()
