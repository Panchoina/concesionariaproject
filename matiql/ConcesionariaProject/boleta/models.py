from django.db import models

# Create your models here.

class boleta(models.Model):
    folio = models.IntegerField(primary_key=True,max_length=10)
    monto = models.IntegerField(max_length=15)
    direccion = models.CharField(max_length=50)
    fono = models.IntegerField(max_length=9)
    fonocliente = models.IntegerField()
    vendedor = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
