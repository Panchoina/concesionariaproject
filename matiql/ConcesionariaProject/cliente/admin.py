from django.contrib import admin
from cliente.models import Cliente
from vehiculo.models import Vehiculo
from empleado.models import Empleado
# registramos el modelo para ser vistod desde el admin

admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Empleado)