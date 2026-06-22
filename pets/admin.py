from django.contrib import admin
from .models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'age', 'gender', 'vaccinated', 'owner', 'created_at')
    list_filter = ('species', 'gender', 'vaccinated')
    search_fields = ('name', 'breed', 'species')


admin.site.register(Pet, PetAdmin)
