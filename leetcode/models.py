from django.db import models

# Create your models here.
class Leetcode(models.Model):
    name = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    rating = models.IntegerField()