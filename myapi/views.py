from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse

from myapi.models import Food_Db


def index(request):
    feed= Food_Db.objects.all()
    foodlist= list()
    for item in Food_Db.objects.all():
        current_food= {
            "name": item.fname,
            "price": item.price
        }
        foodlist.append(current_food)
        # print(item.fname)
    return JsonResponse(foodlist,safe=False)
