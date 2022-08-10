from django.shortcuts import render, redirect
from .models import Professor, Course, Comment


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