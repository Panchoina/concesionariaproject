from django.db import models

class Cliente(models.Model):
    rut = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    FonoCliente = models.PositiveIntegerField()
    gmail = models.CharField(max_length=50)
    password_cliente = models.CharField(max_length=50)  # Aquí sigue como estaba antes
    FechaNacimiento = models.DateField(blank=True)

    def __str__(self):
        return f"{self.rut} - {self.nombre} {self.apellido}"

    class Meta:
        db_table = "Cliente"
