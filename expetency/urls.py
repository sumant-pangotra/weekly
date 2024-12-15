from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_life_expetency_data, name="get_life_expetency_data"),
    path("weeks", views.get_weeks, name="get_weeks"),
    path("country", views.get_countries, name="get_countries"),
    path("gender", views.get_genders, name="get_genders"),
]
   