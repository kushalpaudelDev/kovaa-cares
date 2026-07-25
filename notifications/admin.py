from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'is_read', 'created_at')
    list_display_links = ('title',)
    list_filter = ('is_read',)
    search_fields = ('title', 'message', 'user__username')
    date_hierarchy = 'created_at'
    autocomplete_fields = ('user',)
    list_per_page = 25
    ordering = ('-created_at',)
