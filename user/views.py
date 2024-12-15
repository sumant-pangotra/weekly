# https://radixweb.com/blog/create-rest-api-using-django-rest-framework
# https://github.com/encode/django-rest-framework/issues/4920#issuecomment-281730337
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import AppUserSerializer
from .models import AppUser
from rest_framework import generics
from datetime import datetime


# Create your views here.z
@api_view(['GET','POST'])
def app_users(request):
    if request.method == "GET":
        return get_app_users(request)

    if request.method == "POST":
        return post_app_user(request)

@api_view(['GET','PUT'])
def app_user(request,app_user_id):
    if request.method == "GET":
        return get_app_user(request,app_user_id)
    if request.method == "PUT":
        return put_app_user(request,app_user_id)

    

def get_app_users(request):
    app_users = AppUser.objects.all()
    serialized_app_users = AppUserSerializer(app_users, many=True)
    return Response(serialized_app_users.data)


def post_app_user(request):
    serialized_app_user = AppUserSerializer(data = request.data)
    if serialized_app_user.is_valid():
        serialized_app_user.save()
    return Response(serialized_app_user.data)



class AppUserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    lookup_field = "userId"

@api_view(['GET'])
def get_weeks(request,userId):
    user = AppUser.objects.get(userId=userId)
    print(user.__dict__)
    life_expetency_weeks = (user.life_expetency_years * 365) // 7
    now = datetime.utcnow().date()
    delta = now - user.date_of_birth
    return Response({"weeksLived":delta.days // 7, "totalWeeks":life_expetency_weeks})





