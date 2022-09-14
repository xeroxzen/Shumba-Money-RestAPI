from django.contrib import admin

# Register your models here.
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'country_of_residence', 'password')
    search_fields = ('id', 'first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'country_of_residence')



admin.site.register(Customer, CustomerAdmin)
