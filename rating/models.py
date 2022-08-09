from django.db import models

# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length=255)
    overall = models.FloatField()
    easy = models.FloatField()
    knowledge = models.FloatField()
    fun = models.FloatField()


class Course(models.Model):
    name = models.CharField(max_length=255)
    professors = models.ManyToManyField(Professor)
