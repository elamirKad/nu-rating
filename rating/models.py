from django.db import models

# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length=5550)



class Course(models.Model):
    name = models.CharField(max_length=5550)
    professors = models.ManyToManyField(Professor)

class Comment(models.Model):
    text = models.TextField()
    prof = models.CharField(max_length=5550, default=None)
    easy = models.FloatField(default=0.0)
    knowledge = models.FloatField(default=0.0)
    fun = models.FloatField(default=0.0)
    comment_rating = models.IntegerField(default=0)

class CourseDescription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=55500)
    ects = models.IntegerField()
    school = models.CharField(max_length=55500)
    department = models.CharField(max_length=55500)
    description = models.TextField()
    prereq = models.CharField(max_length=55500)
    coreq = models.CharField(max_length=55500)
    antireq = models.CharField(max_length=55500)
