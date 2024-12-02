from django.db import models
from cliente.models import Cliente  # Asegúrate de importar el modelo Cliente

class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    descripcion = models.TextField(max_length=300)
    precio = models.PositiveIntegerField()
    propietario = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relación con Cliente

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"
