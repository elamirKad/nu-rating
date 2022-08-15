from django.http import JsonResponse
from django.shortcuts import render, redirect
from leetcode.models import *
from leetcode.leetcodeapi import return_rating
import time
# Create your views here.
def main(request):
    if request.method == "POST":
        l = Leetcode(name=request.POST.get('name'), link=request.POST.get('link'), rating=return_rating(request.POST.get('link')))
        l.save()
        return redirect('/leetcode/')
    else:
        leet = Leetcode.objects.all().order_by('-rating')
        dic = {
            'courses': leet
        }
        return render(request,'main.html', dic)


def update(request):
    start_time = time.time()
    leet = Leetcode.objects.all()
    for l in leet:
        try:
            l.rating = return_rating(l.link)
            l.save()
        except:
            l.rating = 0
            l.save()
    elapsed_time = time.time() - start_time
    return JsonResponse({"Success, it took": str(elapsed_time) + " seconds"})