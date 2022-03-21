from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.search_result, name = 'search'),
]
