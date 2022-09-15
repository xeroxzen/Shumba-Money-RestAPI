from django.contrib import admin
from .models import Recipient

@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'country_of_residence')
    search_fields = ('first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'country_of_residence')
    list_per_page = 30