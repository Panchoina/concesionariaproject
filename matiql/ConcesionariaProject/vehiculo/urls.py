from django.contrib import admin
from django.urls import include, path
from vehiculo import views

urlpatterns = [
    path('crear_vehiculo/',views.crear_vehiculo,name='crear_vehiculo'),
    path('listarAutos/', views.listarAutos, name='listarAutos'),
    path('ActualizarVehiculo/<int:id>',views.ActualizarVehiculo,name='ActualizarVehiculo'),
    path('EliminarVehiculo/<int:id>/',views.EliminarVehiculo,name='EliminarVehiculo'),
]