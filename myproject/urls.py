from django.contrib import admin
from django.urls import path
from django.views.generic import ListView, DetailView
from appshop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('profile', views.profile),
    path('posts', views.posts),
    path('newpost', views.newpost),
    path("postinfo/<int:id>/", views.postinfo),
]
