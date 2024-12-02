from django.db import models

# Create your models here.

# Empleado, supervisores, moderadores de contenido.
class Empleado(models.Model):
    rut = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField( max_length=50)
    FonoEmpleado = models.PositiveIntegerField()
    gmail = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    contraseña = models.CharField( max_length=16)
    FechaNacimiento = models.DateField(blank=True)

    def __str__(self):
        return f"{self.rut}"
    class Meta:
        db_table = "Empleado"