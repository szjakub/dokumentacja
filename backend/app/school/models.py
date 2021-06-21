from project import settings
from django.db import models


class School(models.Model):
    principal = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    school_name = models.CharField(max_length=100, unique=True)
    school_address = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return str(self.school_name)


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
    school_class = models.ForeignKey(Class, related_name='students', on_delete=models.CASCADE)

    objects = models.Manager()


class Teacher(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school = models.ForeignKey(School, related_name='teachers', on_delete=models.CASCADE)

    objects = models.Manager()
