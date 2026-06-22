from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Kovaa Cares Admin"
admin.site.site_title = "Kovaa Cares Portal"
admin.site.index_title = "Welcome to Kovaa Cares Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('pets/', include('pets.urls')),
    path('appointments/', include('appointments.urls')),
    path('reviews/', include('reviews.urls')),
]