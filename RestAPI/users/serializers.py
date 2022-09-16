from django.contrib.auth import get_user_model # new

from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ('is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined', 'groups', 'user_permissions')


class UserSerializer(serializers.ModelSerializer): #new
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'middle_name', 'first_name', 'last_name', 'email',  'balance', 'beneficiary', 'password']