from django.contrib import admin
from .models import Professor, Course, Comment, CourseDescription

# Register your models here.
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(CourseDescription)