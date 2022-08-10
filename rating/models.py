from django.db import models

# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length=255)



class Course(models.Model):
    name = models.CharField(max_length=255)
    professors = models.ManyToManyField(Professor)

class Comment(models.Model):
    text = models.TextField()
    prof = models.CharField(max_length=40, default=None)
    easy = models.FloatField(default=0.0)
    knowledge = models.FloatField(default=0.0)
    fun = models.FloatField(default=0.0)