# Multiple Questions: Add imports here
from django.http import HttpResponseNotAllowed

from django.http import JsonResponse, Http404
from assessment.models import Fruit, fruit_to_dict


import json
from http import HTTPStatus
from django.http import HttpResponseNotAllowed, JsonResponse, HttpResponse
from django.urls import reverse

from django.shortcuts import get_object_or_404

def fruit_list(request):
    # Question 1: Complete this function body
    if request.method == "GET":
        return handle_list_get()

    if request.method == "POST":
        return handle_list_post(request.body)

    return HttpResponseNotAllowed(["GET", "POST"])


def fruit_detail(request, pk):
    # Question 2: Complete this function body
    if request.method == "GET":
        return handle_detail_get(pk)

    if request.method == "PUT":
        return handle_detail_put(pk, request.body)

    if request.method == "DELETE":
        return handle_detail_delete(pk)

    return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])


def handle_list_get():
    # Question 3: Complete this function body
    fruits = Fruit.objects.all()
    fruit_list = [fruit_to_dict(fruit) for fruit in fruits]
    return JsonResponse({"data": fruit_list})

def handle_detail_get(pk):
    # Question 3: Complete this function body
    try:
        fruit = Fruit.objects.get(pk=pk)
        fruit_dict = fruit_to_dict(fruit)
        return JsonResponse(fruit_dict)
    except Fruit.DoesNotExist:
        raise Http404("Fruit not found")


def handle_list_post(body):
    # Question 4: Complete this function body
    data = json.loads(body)
    f = Fruit.objects.create(**data)
    return HttpResponse(
        status=HTTPStatus.CREATED,
        headers={"Location": reverse("api_fruit_detail", args=(f.pk,))},
    )

def handle_detail_put(pk, body):
    # Question 5: Complete this function body
    f = get_object_or_404(Fruit, pk=pk)
    data = json.loads(body)
    for field, value in data.items():
        setattr(f, field, value)
    f.save()
    return HttpResponse(status=HTTPStatus.NO_CONTENT)

def handle_detail_delete(pk):
    # Question 5: Complete this function body
    f = get_object_or_404(Fruit, pk=pk)
    f.delete()
    return HttpResponse(status=HTTPStatus.NO_CONTENT)