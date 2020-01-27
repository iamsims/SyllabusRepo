from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home ),#go to select part , for now only this to be handled
]
