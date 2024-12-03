from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from vehiculo.models import Vehiculo
from vehiculo.forms import VehiculoForm
from django.contrib.auth.decorators import permission_required
# Create your views here.

# Registrar vehículo

@permission_required(['vehiculo.add_vehiculo'], login_url='/accounts/login/', raise_exception=True)
def crear_vehiculo(request):
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            # Redirige o muestra algún mensaje de éxito
    else:
        formulario = VehiculoForm()

    return render(request, 'cliente/Vender.html', {'formulario': formulario})

@permission_required(['vehiculo.view_vehiculo'], login_url='/accounts/login/', raise_exception=True)
def listarAutos(request):
    vehiculo = Vehiculo.objects.all()
    data = {'lista':vehiculo}
    return render(request,'cliente/Inicio.html',data)