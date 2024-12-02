from django.contrib import admin
from django.urls import include, path
from empleado import views

from django.urls import path
from . import views

urlpatterns = [
    path('crearempleado/', views.CrearEmpleado, name='crearempleado'),
    path('listar/', views.ListarEmpelados, name='listar_empleados'),
    path('actualizar/<int:id>/', views.ActualizarEmpleados, name='actualizar_empleados'),
    path('imprimir/', views.ImprimirEmpleados, name='imprimir_empleados'),
]
