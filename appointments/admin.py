from django.apps import apps
from django.contrib import admin
from .models import Appointment


class PaymentInline(admin.TabularInline):
    model = apps.get_model('payments', 'Payment')
    extra = 0
    readonly_fields = ('amount', 'payment_method', 'status', 'paid_at')
    can_delete = False
    show_change_link = True


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pet', 'service', 'appointment_date', 'status', 'created_at')
    list_display_links = ('pet', 'service')
    list_filter = ('status', 'service', 'appointment_date')
    search_fields = ('pet__name', 'service__name', 'notes')
    date_hierarchy = 'appointment_date'
    autocomplete_fields = ('pet', 'service')
    inlines = [PaymentInline]
    list_per_page = 25
    ordering = ('-appointment_date',)


admin.site.register(Appointment, AppointmentAdmin)
