from django.contrib import admin
from .models import Professor, Course

# Register your models here.
admin.site.register(Professor)
admin.site.register(Course)