from django.http import JsonResponse
from django.shortcuts import render, redirect
from leetcode.models import *
from leetcode.leetcodeapi import *
import time
from datetime import datetime
from django.db.models import Sum

# Create your views here.
def main(request):
    if request.method == "POST":
        if not Leetcode.objects.filter(link=request.POST.get('link')).exists():
            rating, contests_num, percentage = return_rating(request.POST.get('link'))
            easy, medium, hard = return_tasks(request.POST.get('link'))
            l = Leetcode(name=request.POST.get('name'), link=request.POST.get('link'), rating=rating, change=rating, total=easy+medium+hard, easy=easy, medium=medium,
                         hard=hard, contests_count=contests_num, top_percentage=percentage, img_url=get_image(request.POST.get('link')))
            l.save()
        return redirect('/leetcode/')
    else:
        leet = Leetcode.objects.all().order_by('-rating')
        dic = {
            'leetcodes': leet,
        }
        return render(request,'main.html', dic)


def update(request):
    start_time = time.time()
    leet = Leetcode.objects.all()
    for l in leet:
        rating, contests_num, percentage = return_rating(l.link)
        easy, medium, hard = return_tasks(l.link)
        l.easy, l.medium, l.hard, l.total = easy, medium, hard, easy+medium+hard
        try:
            l.rating = rating
            l.contests_count = contests_num
            l.top_percentage = percentage
        except:
            l.rating = 0
            l.contests_count = 0
            l.top_percentage = 0
        l.save()
    elapsed_time = time.time() - start_time
    return redirect('/leetcode/')

def user(request, username):
    l = Leetcode.objects.get(link=username)
    l_history = ContestUser.objects.filter(user=l).order_by('-contest__starttime')
    for lh in l_history:
        lh.contest.starttime = datetime.fromtimestamp(int(lh.contest.starttime)).strftime("%m.%d.%y")
    dic = {
        "leet": l,
        "history": l_history
    }
    return render(request, 'user.html', dic)

def add_contests(request):
    import time
    start_time = time.time()
    for i in range(1, 3):
        total, title, times = return_contests('sulrz', i)
        if not Contest.objects.filter(title=title).exists():
            c = Contest(totalPorblems=total, title=title, starttime=times)
            c.save()
    elapsed_time = time.time() - start_time
    return JsonResponse({'Success': f'it took {elapsed_time}'})

def update_users(request):
    import time
    start_time = time.time()
    leetcodes = Leetcode.objects.all()
    for leet in leetcodes:
        print(f"{leet.name} started")
        for i in range(1, 20):
            try:
                attended, trend, finish, solved, rating, ranking, title = return_user(leet.name, i)
                if not ContestUser.objects.filter(user=leet, contest=Contest.objects.get(title=title)).exists():
                    if attended:
                        print(title)
                        c = Contest.objects.get(title=title)
                        c_u = ContestUser(user=leet, contest=c, attended=attended, trend=trend, finish=finish, solved=solved, rating=rating, ranking=ranking)
                        c_u.save()
                        print(f"{leet.name} contest added")
                    else:
                        print("Not attended")
                else:
                    print(title + " exists")
            except:
                pass
    elapsed_time = time.time() - start_time
    return JsonResponse({'Success': f'it took {elapsed_time}'})