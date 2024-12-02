from django.utils import timezone
from django.db import models

from empleado.models import Empleado
from cliente.models import Cliente

# Create your models here.

#boleta donde se guardara información general de la compra hecha por el cliente

class boleta(models.Model):
    folio = models.PositiveIntegerField(primary_key=True)
    monto = models.PositiveIntegerField()
    direccion = models.CharField(max_length=50)
    fecha = models.DateTimeField(default=timezone.now)
    fono = models.PositiveIntegerField()
    FonoEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="boletas_fono_empleado")
    FonoCliente = models.ForeignKey(Cliente,  on_delete=models.CASCADE, related_name="boletas_fono_cliente")
    vendedor = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.folio}"
    class Meta:
        db_table = "Boleta"