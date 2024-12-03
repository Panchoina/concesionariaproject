from django.contrib import admin
from django.urls import include, path
from empleado import views

from django.urls import path
from . import views

urlpatterns = [
    path('RegistroEmpleado/', views.RegistroEmpleado, name='RegistroEmpleado'),
    path('listar/', views.listar, name='listar'),
    path('actualizar/<int:id>/', views.ActualizarEmpleado, name='actualizar_empleados'),
    path('eliminarempleado/<int:id>',views.EliminarEmpleado,name='eliminarempleado'),
    path('imprimir/', views.ImprimirEmpleados, name='imprimir_empleados'),
]
