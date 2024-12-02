from django.contrib import admin
from django.urls import include, path
from vehiculo import views

urlpatterns = [
    path('VenderAuto/',views.VenderAuto,name='VenderAuto'),
]