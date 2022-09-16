from django.contrib import admin
from .models import Transaction

# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'amount', 'created_at', 'status', 'transaction_type', 'reference')
    search_fields = ('sender', 'recipient', 'amount', 'created_at', 'status', 'transaction_type', 'reference')
    list_per_page = 30
