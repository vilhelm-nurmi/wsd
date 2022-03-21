from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('shop/error', views.error, name = 'error'),
    path('shop/cancel', views.cancel, name = 'cancel'),
    path('shop/success', views.success, name = 'success'),

]
