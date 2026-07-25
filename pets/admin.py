from django.contrib import admin
from django.apps import apps
from .models import Pet

class AppointmentInline(admin.TabularInline):
    model = apps.get_model('appointments', 'Appointment')
    extra = 0
    fields = ('service', 'appointment_date', 'status')
    readonly_fields = ('service', 'appointment_date', 'status')
    can_delete = False
    show_change_link = True

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'age', 'gender', 'vaccinated', 'owner', 'created_at')
    list_display_links = ('name',)
    list_filter = ('species', 'gender', 'vaccinated')
    search_fields = ('name', 'breed', 'species', 'owner__username')
    autocomplete_fields = ('owner',)
    inlines = [AppointmentInline]
    list_per_page = 25
    ordering = ('-created_at',)
