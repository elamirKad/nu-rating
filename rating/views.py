from django.shortcuts import render
from .models import Professor, Course


# Create your views here.
def main(request):
    courses = Course.objects.all()
    dic = {
        'courses': courses
    }
    return render(request, 'index.html', dic)