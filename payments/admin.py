from django.contrib import admin
from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'amount', 'payment_method', 'status', 'paid_at')
    list_display_links = ('appointment',)
    list_filter = ('status', 'payment_method')
    search_fields = ('appointment__pet__name', 'transaction_id')
    date_hierarchy = 'paid_at'
    autocomplete_fields = ('appointment',)
    list_per_page = 25
    ordering = ('-paid_at',)


admin.site.register(Payment, PaymentAdmin)
