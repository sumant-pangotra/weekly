from django.urls import path
from . import views

urlpatterns = [
    path("", views.app_users, name="create_get_app_user"),
    path("<int:userId>", views.AppUserDetails.as_view(), name="app_user_by_userId"),
    path("<int:userId>/weeks", views.get_weeks, name="get_weeks")
]