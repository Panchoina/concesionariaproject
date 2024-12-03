from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from vehiculo.forms import VehiculoForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Vehiculo
from .forms import VehiculoForm
import csv
from django.http import HttpResponse


@permission_required(['vehiculo.add_vehiculo'], login_url='/accounts/login/', raise_exception=True)
def VenderAuto(request):
    form = VehiculoForm()
    data = {
        'titulo': 'Registrar Vehículo',
        'formulario': form,
    }

    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)  # Evitamos guardar el vehículo inmediatamente
            
            # Asigna un propietario explícito. Asegúrate de que el ID del propietario exista en tu base de datos
            propietario_id = request.POST.get('propietario')  # Ajusta según cómo recibes este dato
            if propietario_id:
                vehiculo.propietario_id = propietario_id
                vehiculo.save()  # Ahora sí guardamos el vehículo
                messages.success(request, 'Vehículo registrado con éxito')
                return redirect('listar_vehiculos')
            else:
                messages.error(request, 'Debes seleccionar un propietario válido.')
        else:
            data['formulario'] = form

    return render(request, 'cliente/Vender.html', data)



@permission_required(['vehiculo.view_vehiculo'], login_url='/accounts/login/', raise_exception=True)
def ListarVehiculos(request):
    vehiculos = Vehiculo.objects.all()
    data = {
        'titulo': 'Lista de Vehículos',
        'lista': vehiculos,
    }
    return render(request, 'vehiculo/verVehiculos.html', data)


@permission_required(['vehiculo.change_vehiculo'], login_url='/accounts/login/', raise_exception=True)
def ActualizarVehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, pk=id)
    form = VehiculoForm(instance=vehiculo)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo actualizado con éxito')
            return redirect('listar_vehiculos')

    data = {
        'titulo': 'Editar Vehículo',
        'formulario': form,
    }
    return render(request, 'vehiculo/agregarVehiculo.html', data)


@permission_required(['vehiculo.delete_vehiculo'], login_url='/accounts/login/', raise_exception=True)
def EliminarVehiculo(request, id):
    vehiculo = get_object_or_404(Vehiculo, pk=id)
    vehiculo.delete()
    messages.success(request, 'Vehículo eliminado con éxito')
    return redirect('listar_vehiculos')


@permission_required(['vehiculo.view_vehiculo'], login_url='/accounts/login/', raise_exception=True)
def ExportarVehiculosExcel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="vehiculos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Descripción', 'Marca', 'Modelo', 'Año', 'Precio', 'Propietario'])

    vehiculos = Vehiculo.objects.all().values_list(
        'descripcion', 'marca', 'modelo', 'año', 'precio', 'propietario__nombre'
    )
    for vehiculo in vehiculos:
        writer.writerow(vehiculo)

    return response
