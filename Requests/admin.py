from django.contrib import admin
from .models import Request
# Register your models here.
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'DateTime', 'PlayerID', 'AccountTitle', 'AccountNumber', 'PaymentMethod', 'Amount', 'Status')
    search_fields = ('PlayerID', 'AccountTitle', 'PaymentMethod')
    list_filter = ('Status', 'PaymentMethod')