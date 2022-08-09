from django.shortcuts import render
from .models import Professor, Course


# Create your views here.
def main(request):
    courses = Course.objects.all()
    dic = {
        'courses': courses
    }
    return render(request, 'index.html', dic)

def course(request, course_name):
    course = Course.objects.get(name=course_name)
    profs = course.professors.all()
    dic = {
        'course_name': course_name,
        'profs': profs
    }
    return render(request, 'course.html', dic)

def professor(request, prof):
    profess = Professor.objects.get(name=prof)
    print(profess.overall)
    dic = {
        'profess': profess
    }
    return render(request, 'prof.html', dic)