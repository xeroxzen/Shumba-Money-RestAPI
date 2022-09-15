from re import I
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Customer
from .forms import CustomerCreationForm, CustomerChangeForm

@admin.register(Customer)
class UserAdmin(BaseUserAdmin):
    add_form = CustomerCreationForm
    form = CustomerChangeForm
    list_display = ('first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'country_of_residence')
    search_fields = ('first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'country_of_residence')
    list_per_page = 30
    # fieldsets = (
    #     (None, {'fields': ('first_name')}),
    #     ('Personal Info', 
    #     {'fields': ('first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'country_of_residence')
    #     }),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser'),
    #     }),
    #     ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    # )
    list_filter = ('date_joined', 'is_active', 'is_staff', 'is_superuser', 'is_superuser')



# admin.site.register(Customer, CustomerAdmin)
