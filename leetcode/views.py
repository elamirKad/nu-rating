from django.http import JsonResponse
from django.shortcuts import render, redirect
from leetcode.models import *
from leetcode.leetcodeapi import *
import time
from django.db.models import Sum

# Create your views here.
def main(request):
    if request.method == "POST":
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