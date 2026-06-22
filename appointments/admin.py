from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pet', 'service', 'appointment_date', 'status', 'created_at')
    list_filter = ('status', 'appointment_date')
    search_fields = ('pet__name', 'service', 'notes')


admin.site.register(Appointment, AppointmentAdmin)
