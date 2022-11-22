from django.contrib import admin
from django.urls import path
from django.views.generic import ListView, DetailView
from appshop import views
from appshop.models import Products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('profile', views.profile),
    path('products', views.products),
    path('create', views.create)
]
