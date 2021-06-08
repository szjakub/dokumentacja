import uuid
from hashlib import md5

from django.contrib.auth.models import User
from django.db import models


class School(models.Model):
    principal = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    principal_email = models.EmailField()
    school_name = models.CharField(max_length=100)
    school_address = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)

    objects = models.Manager()

    def save(self, *args, **kwargs):
        if self.verified:
            username = uuid.uuid4()
            password = md5(str(username)).hexdigest()
            user = User.objects.create_user(
                username=username, password=password, email=self.principal_email)
            user.save()
            self.principal = user
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school_class = models.ForeignKey(Class, related_name='students', on_delete=models.CASCADE)

    objects = models.Manager()


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    school = models.ForeignKey(School, related_name='teachers', on_delete=models.CASCADE)

    objects = models.Manager()
