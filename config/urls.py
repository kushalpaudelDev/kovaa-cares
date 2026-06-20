from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

admin.site.site_header = "Kovaa Cares Admin"
admin.site.site_title = "Kovaa Cares Portal"
admin.site.index_title = "Welcome to Kovaa Cares Dashboard"

# simple dashboard (no model import)
def dashboard(request):
    return HttpResponse("Kovaa Cares Dashboard Working")

urlpatterns = [
    path('admin/dashboard/', dashboard),
    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('pets/', include('pets.urls')),
    path('appointments/', include('appointments.urls')),
]