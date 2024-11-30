from django.db import models

# Create your models here.

class cliente(models.Model):
    rut = models.IntegerField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField( max_length=50)
    fono = models.IntegerField(max_length=9)
    gmail = models.CharField(max_length=50)
    contraseña = models.CharField( max_length=50)

    def __str__(self):
        return f"{self.nombre}"
    class Meta:
        db_table = "Cliente"