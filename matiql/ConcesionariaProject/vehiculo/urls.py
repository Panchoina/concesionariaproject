from django.contrib import admin
from django.urls import include, path
from vehiculo import views

urlpatterns = [
    path('crear_vehiculo/',views.crear_vehiculo,name='crear_vehiculo'),
]