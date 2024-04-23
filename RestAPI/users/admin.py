from re import I
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Customer
from .forms import CustomerCreationForm, CustomerChangeForm

@admin.register(Customer)
class UserAdmin(BaseUserAdmin):
    add_form = CustomerCreationForm
    form = CustomerChangeForm
    list_display = ('username','first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'country_of_residence')
    search_fields = ('username','first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'country_of_residence')
    list_per_page = 30
    list_filter = ('date_joined', 'is_active', 'is_staff', 'is_superuser', 'is_superuser')
