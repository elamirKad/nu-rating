from django.db import models

# Create your models here.
class Leetcode(models.Model):
    name = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    rating = models.IntegerField(default=0)
    change = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    easy = models.IntegerField(default=0)
    medium = models.IntegerField(default=0)
    hard = models.IntegerField(default=0)
    contests_count = models.IntegerField(default=0)
    top_percentage = models.FloatField(default=0.0)
    img_url = models.CharField(max_length=10000, default='')

class Contest(models.Model):
    totalPorblems = models.IntegerField()
    title = models.CharField(max_length=1000)
    starttime = models.CharField(max_length=1000)

class ContestUser(models.Model):
    user = models.ForeignKey("Leetcode", on_delete=models.CASCADE)
    contest = models.ForeignKey("Contest", on_delete=models.CASCADE, default=None)
    attended = models.BooleanField(default=False)
    trend = models.CharField(max_length=1000, default='NONE')
    solved = models.IntegerField(default=0)
    finish = models.IntegerField(default=0)
    rating = models.IntegerField(default=1500)
    ranking = models.IntegerField(default=0)
