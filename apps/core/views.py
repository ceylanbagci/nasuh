from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
import core.helper as hlp
import json



def get_districts_from_city(request, city_id=None):
    district_list = hlp.get_list(model_class=District,city__id=city_id).order_by("name")
    return JsonResponse({'district_list': json.dumps([{
                'name': district.name,
                'id': district.id,
            }
            for district in district_list
        ])})
