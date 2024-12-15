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
    return Response(lifeExpetencyService.get_weeks_lived(int(dob[0]),int(dob[1]),int(dob[2]),request.GET.get('country'),request.GET.get('sex')))
    

