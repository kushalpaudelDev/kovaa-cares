from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'created_at')
    list_display_links = ('user',)
    list_filter = ('rating',)
    search_fields = ('user__username', 'comment')
    date_hierarchy = 'created_at'
    autocomplete_fields = ('user',)
    list_per_page = 25
    ordering = ('-created_at',)


admin.site.register(Review, ReviewAdmin)
