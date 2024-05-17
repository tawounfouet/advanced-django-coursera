import datetime

from django.http import HttpResponse
from django.shortcuts import render

from assessment.models import get_test_resources, Resource

# Question 1 & 2: Add your imports here
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

# Question 1: Cache this view
@cache_page(120)
def question1(request):
    # Do not change this function body
    return HttpResponse(datetime.datetime.now().isoformat())


# Question 2: Cache this view, make sure it's different for each user
@cache_page(120)
@vary_on_cookie
def question2(request):
    # Do not change this function body
    return HttpResponse(datetime.datetime.now().isoformat() + str(request.user))

def question3(request):
    # Do not change this function body
    return render(request, "question3.html")


def question4(request):
    test_resources = get_test_resources()

    # Question 4: Add code to insert all test resources at once below

    return HttpResponse(", ".join(map(str, Resource.objects.all())))


def question5(request):
    test_resources = get_test_resources(save_to_db=True)

    # Question 5: Add code to update all test resources then save with a bulk call below

    return HttpResponse(", ".join(map(str, Resource.objects.all())))