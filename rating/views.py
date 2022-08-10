from django.shortcuts import render, redirect
from .models import Professor, Course, Comment
from django.http import JsonResponse
from rating.extract import get_profs_and_courses

# Create your views here.
def main(request):
    if request.method == "GET":
        keywords = request.GET.get('course')

        if keywords:
            data = Course.objects.filter(name__icontains=keywords).order_by('name')
        else:
            data = Course.objects.all().order_by('name')

        dic = {
            'courses': data
        }
        return render(request, 'index.html', dic)
    else:
        courses = Course.objects.all().order_by('name')
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
    if request.method == "POST":
        comment = Comment(text=request.POST.get('comment'), prof=request.POST.get('prof_id'),
                          easy=request.POST.get('easy'), knowledge=request.POST.get('knowledge'), fun=request.POST.get('fun'))
        comment.save()
        return redirect(f'/main/prof/{prof}')
    else:
        profess = Professor.objects.get(name=prof)
        comments = Comment.objects.filter(prof=profess.id)
        if comments:
            overall, easy, knowledge, fun, amount = calc(comments)
        else:
            overall, easy, knowledge, fun, amount = 0, 0, 0, 0, 0
        dic = {
            'profess': profess,
            'overall': overall,
            'easy': easy,
            'knowledge': knowledge,
            'fun': fun,
            'comments': comments
        }
        return render(request, 'prof.html', dic)

def calc(comments):
    overall = 0
    easy = 0
    knowledge = 0
    fun = 0
    amount = 0
    for comm in comments:
        amount += 1
        easy += comm.easy
        knowledge += comm.knowledge
        fun += comm.fun
    easy = round(easy / amount, 1)
    knowledge = round(knowledge / amount, 1)
    fun = round(fun / amount, 1)
    overall = round((easy + knowledge + fun) / 3, 1)
    return overall, easy, knowledge, fun, amount


def register(request):
    response_data = get_profs_and_courses()
    for r in response_data:
        try:
            prof = Professor.objects.get(name=r)
        except:
            prof = None
        if prof:
            for course in response_data[r]:
                course = course.replace('/', ' OR ')
                try:
                    c = Course.objects.get(name=course)
                except:
                    c = None
                if c:
                    c.professors.add(prof)
                    print("Added course", course, " to the prof ", r)
                else:
                    c = Course(name=course)
                    c.save()
                    c.professors.add(prof)
                    print("Created course ", course, " and added to the prof ", r)
        else:
            prof = Professor(name=r)
            prof.save()
            print("Created ", r)
        print(response_data[r], r)
    return JsonResponse(response_data)