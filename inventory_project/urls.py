from django.contrib import admin
from django.urls import path
from inventory import views
from django.shortcuts import render

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('item/<int:pk>/delete/', views.item_delete, name='item_delete'),
    path('admin/', admin.site.urls),
    path('items/', views.item_list, name='item_list'),
    path('item/add/', views.item_add, name='item_add'),
    path('item/<int:pk>/edit/', views.item_edit, name='item_edit'),
    path('', views.home, name='home'),
    path('inventory-report/', views.inventory_report, name='inventory_report'),
]

def home(request):
    return render(request, 'home.html')  # Ensure you have a 'home.html' template

