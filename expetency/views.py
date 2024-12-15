from django.shortcuts import render
from .service import lifeExpetencyService
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime


@api_view(['GET'])
def get_life_expetency_data(request):
    
    data = lifeExpetencyService.getLatestByRegion(request.GET.get('country'),request.GET.get('sex'))
    print(data)
    return Response({"data":data})

@api_view(['GET'])
def get_countries(request):
    return Response(lifeExpetencyService.getCountryCodes())

@api_view(['GET'])
def get_genders(request):
    return Response(lifeExpetencyService.getSexCodes())

    

@api_view(['GET'])
def get_weeks(request):
    dob = request.GET.get('dob')
    dob = dob.split("-")
    if not len(dob) == 3:
        raise Exception("Invalid Date Of Birth")
    life_expetency_weeks = (75 * 365) // 7
    now = datetime.utcnow().date()
    delta = now - datetime(int(dob[2]),int(dob[1]),int(dob[0])).date()
    return Response({"weeksLived":delta.days // 7, "totalWeeks":life_expetency_weeks})
    

