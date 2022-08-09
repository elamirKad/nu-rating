from django.db import models

# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length=255)
    overall = models.FloatField(default=0.0)
    easy = models.FloatField(default=0.0)
    knowledge = models.FloatField(default=0.0)
    fun = models.FloatField(default=0.0)


class Course(models.Model):
    name = models.CharField(max_length=255)
    professors = models.ManyToManyField(Professor)
