from rest_framework import serializers
from .models import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ("userId","first_name","last_name","email_id","date_of_birth","life_expetency_years")