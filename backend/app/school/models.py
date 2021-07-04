from project import settings
from django.db import models
from django.utils.translation import ugettext as _

from .fields import DayOfTheWeekField


class School(models.Model):
    school_name = models.CharField(max_length=100, unique=True)
    school_address = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return str(self.school_name)


class SchoolClass(models.Model):
    school = models.ForeignKey(School, related_name='classes', on_delete=models.CASCADE)
    yearbook = models.SmallIntegerField()
    class_label = models.CharField(max_length=2)

    objects = models.Manager()

    def __str__(self):
        return f'{self.yearbook}{self.class_label} in {self.school.name}'

    class Meta:
        verbose_name_plural = 'class'
        unique_together = ['school', 'yearbook', 'class_label']


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    school = models.ForeignKey(School, related_name='school_students', on_delete=models.CASCADE)

    school_class = models.ForeignKey(SchoolClass, related_name='class_students', on_delete=models.CASCADE)

    objects = models.Manager()


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    school = models.ForeignKey(School, related_name='school_teachers', on_delete=models.CASCADE)

    objects = models.Manager()


class Principal(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    school = models.OneToOneField(School, related_name='school_principal', on_delete=models.CASCADE)

    objects = models.Manager()


class Subject(models.Model):
    school = models.ForeignKey(School, related_name='school_subjects', on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)

    objects = models.Manager()


class Lesson(models.Model):
    school = models.ForeignKey(School, related_name='school_lessons', on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, related_name='class_lessons', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day = DayOfTheWeekField()
    start_time = models.TimeField()
    duration = models.SmallIntegerField(default=45)

    objects = models.Manager()
