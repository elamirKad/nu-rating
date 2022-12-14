from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.decorators import cache

from nurating import settings
from .models import Professor, Course, Comment, CourseDescription
from django.http import JsonResponse, HttpResponse
from rating.extract import get_profs_and_courses
from rating.courses_details_scrapper import get_course_details
import time


# Create your views here.
def main(request):
    if request.method == "GET":
        prof_bool = False
        keywords = request.GET.get('course')
        if request.GET.get('search_type') == 'course':
            if keywords:
                data = Course.objects.filter(name__icontains=keywords).order_by('name')
            else:
                #data = cache.get('data')
                #if not data:
                data = Course.objects.all().order_by('name')
                #cache.set('data', data, 60*60*8)
        elif request.GET.get('search_type') == 'prof':
            prof_bool = True
            if keywords:
                data = Professor.objects.filter(name__icontains=keywords).order_by('name')
            else:
                #data = cache.get('data')
                #if not data:
                data = Professor.objects.all().order_by('name')
                #cache.set('data', data, 60*60*8)
        else:
            data = Course.objects.all().order_by('name')

        dic = {
            'courses': data,
            'prof_bool': prof_bool
        }
        return render(request, 'index.html', dic)
    else:
        #courses = cache.get('courses')
        #if not courses:
        courses = Course.objects.all().order_by('name')
            #cache.set('courses', courses, 60 * 60 * 8)
        dic = {
            'courses': courses
        }
        return render(request, 'index.html', dic)

def course(request, course_name):
    course = Course.objects.get(name=course_name)
    profs = course.professors.all().order_by('name')
    try:
        details = CourseDescription.objects.get(course=course)
    except:
        details = None

    prof_dic = {}
    for prof in profs:
        comments = Comment.objects.filter(prof=prof.id)
        if comments:
            overall, easy, knowledge, fun, amount = calc(comments)
            prof_dic[prof.id] = overall
        else:
            overall, easy, knowledge, fun, amount = 0, 0, 0, 0, 0
            prof_dic[prof.id] = overall

    dic = {
        'course_name': course_name,
        'profs': profs,
        'data': details,
        'prof_rating': prof_dic
    }
    return render(request, 'course.html', dic)

def professor(request, prof):
    if request.method == "POST":
        if 'rating_change' in request.POST:
            if request.session.get(request.POST.get('comm_id'), False):
                return HttpResponse("You have already voted")
            comment = Comment.objects.get(id=int(request.POST.get('comm_id')))
            if request.POST.get('rating_change') == "plus":
                comment.comment_rating += 1
            elif request.POST.get('rating_change') == "minus":
                comment.comment_rating -= 1
            request.session[request.POST.get('comm_id')] = True
            comment.save()
            return redirect(f'/main/prof/{prof}')

        if request.session.get(request.POST.get('prof_id'), False):
            return HttpResponse("You have already commented")
        comment = Comment(text=request.POST.get('comment'), prof=request.POST.get('prof_id'),
                        easy=request.POST.get('easy'), knowledge=request.POST.get('knowledge'), fun=request.POST.get('fun'))
        comment.save()
        request.session[request.POST.get('prof_id')] = True
        return redirect(f'/main/prof/{prof}')
    else:
        profess = Professor.objects.get(name=prof)
        comments = Comment.objects.filter(prof=profess.id).order_by('-comment_rating')
        all_courses = profess.course_set.all()
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
            'comments': comments,
            'courses': all_courses
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


def register_courses_details(request):
    start_time = time.time()
    courses = Course.objects.all().order_by('name')
    for course in courses:
        print("Processing", course.name)
        data = get_course_details(course.name)
        try:
            course_desc = CourseDescription.objects.get(course=course)
        except:
            course_desc = None
        if not course_desc:
            try:
                c = CourseDescription(course=course, title=data['TITLE'], ects=int(data['CRECTS']),
                                      school=data['SCHOOL'], department=data['DEPARTMENT'], description=data['SHORTDESC'],
                                      prereq=data['PREREQ'], coreq=data['COREQ'], antireq=data['ANTIREQ'])
                c.save()
            except:
                pass
        else:
            print("Course exists")
    elapsed_time = time.time() - start_time
    return JsonResponse({"Success, it took": str(elapsed_time) + " seconds"})

def check_mail(request):
    subject = 'welcome to GFG world'
    message = f'Hi thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["elamirkad@gmail.com"]
    send_mail(subject, message, email_from, recipient_list)
    return JsonResponse({"Success": 1})

def update_course_description(request):
    start_time = time.time()
    courses = Course.objects.all()
    flag = False
    for course in courses:
        if flag:
            try:
                details = CourseDescription.objects.get(course=course)
                for c in courses:
                    if f"<a href='/main/{c.name}' style='color:#ffd100;'>{c.name}</a>" not in details.prereq:
                        details.prereq = details.prereq.replace(c.name, f"<a href='/main/{c.name}' style='color:#ffd100;'>{c.name}</a>")
                    if f"<a href='/main/{c.name}' style='color:#ffd100;'>{c.name}</a>" not in details.coreq:
                        details.coreq = details.coreq.replace(c.name, f"<a href='/main/{c.name}' style='color:#ffd100;'>{c.name}</a>")
                    if f"<a href='/main/{c.name}' style='color:#ffd100;'>{c.name}</a>" not in details.antireq:
                        details.antireq = details.antireq.replace(c.name, f"<a href='/main/{c.name}' style='color:#ffd100;'>{c.name}</a>")
                    details.save()
                print("Success", course.name)
            except:
                print("Failure", course.name)
        else:
            if course.name == "PHYS 362":
                print("FOUND")
                flag = True
    elapsed_time = time.time() - start_time
    return JsonResponse({"Success, it took": str(elapsed_time) + " seconds"})


def schedule(request):
    if request.method == "POST":
        if 'delete' in request.POST:
            c = Course.objects.get(name=request.POST.get('course_name'))
            c_temp = CourseDescription.objects.get(course=c)
            arr = request.session[request.POST.get('semester')]
            del arr[request.session[request.POST.get('semester')].index(request.POST.get('course_name'))]
            request.session[request.POST.get('semester')] = arr
            request.session[request.POST.get('semester') + "_ects"] -= c_temp.ects
            return redirect("/main/schedule/")

        for key, value in request.POST.items():

            if key in request.session:
                #del request.session[key]
                request.session[key] += [value]
                c = Course.objects.get(name=value)
                c_temp = CourseDescription.objects.get(course=c)
                try:
                    request.session[key+"_ects"] += c_temp.ects
                except:
                    request.session[key + "_ects"] = c_temp.ects
            elif key in [str(i)+"_semester" for i in range(1,9)]:
                #pass
                request.session[key] = [value]
                c = Course.objects.get(name=value)
                c_temp = CourseDescription.objects.get(course=c)
                request.session[key + "_ects"] = c_temp.ects
        return redirect("/main/schedule/")
    else:
        courses = Course.objects.all()
        dic = {
            'courses': courses
        }
        return render(request, 'schedule.html', dic)