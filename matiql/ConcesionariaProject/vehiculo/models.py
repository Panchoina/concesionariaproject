from django.db import models
from cliente.models import Cliente  # Asumiendo que Cliente está en la carpeta cliente

class Vehiculo(models.Model):
    descripcion = models.CharField(max_length=255)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.PositiveIntegerField()  # Cambié a PositiveIntegerField si es necesario
    precio = models.PositiveIntegerField()  # Debería ser un campo numérico
    propietario = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relación con Cliente

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"
