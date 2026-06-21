from django.urls import path
from . import views

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('create/', views.pet_create, name='pet_create'),
    path('update/<int:pk>/', views.pet_update, name='pet_update'),
    path('delete/<int:pk>/', views.pet_delete, name='pet_delete'),
]