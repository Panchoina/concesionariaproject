from django.contrib.auth.models import User
from django.db import models

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    rut = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    FonoEmpleado = models.PositiveIntegerField()
    gmail = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=16)
    FechaNacimiento = models.DateField(blank=True)

    # Relación con User de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rut} - {self.nombre}"

    class Meta:
        db_table = "Empleado"
