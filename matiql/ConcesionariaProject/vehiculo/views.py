from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from vehiculo.forms import VehiculoForm

# Create your views here.

# Registrar vehículo
def VenderAuto(request):
    form = VehiculoForm()
    data = {
        'titulo': 'Crear Cliente',
        'formulario': form,
        'ruta': 'cargos'
    }

    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            cliente = request.user.cliente
            # Guardamos el formulario
            vehiculo = form.save(commit=False)
            # Asignar el propietario al cliente autenticado
            vehiculo.propietario = cliente
            # Mensaje de éxito
            vehiculo.save()
            messages.success(request, 'Cliente creado con éxito!!!')
            # Redirigir al login después de crear el cliente
            return redirect('login')
            
    return render(request, 'cliente/Vender.html', data)