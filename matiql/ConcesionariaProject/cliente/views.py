from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from cliente.forms import ClienteFormRegis
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from vehiculo.models import Vehiculo

# Vista de inicio, redirige si no está autenticado
@login_required(login_url='accounts/login')
def inicio(request):
    return render(request, 'Index.html')

# Vista para la página principal de los clientes, con permisos
@permission_required(['cliente.view_cliente', 'empleado.view_empleado'], login_url='/accounts/login/', raise_exception=True)
def homepag(request):
    # lista de los vehiculos en venta
    
    vehiculos = Vehiculo.objects.all()
    data = {'lista':vehiculos}
    return render(request, "cliente/Inicio.html", data)

# Registro de un cliente
# @permission_required('cliente.add_cliente', login_url='/', raise_exception=True)
def Registro(request):
    form = ClienteFormRegis()
    data = {
        'titulo': 'Crear Cliente',
        'formulario': form,
        'ruta': 'cargos'
    }

    if request.method == 'POST':
        form = ClienteFormRegis(request.POST)
        if form.is_valid():
            # Guardamos el formulario
            form.save()
            # Mensaje de éxito
            messages.success(request, 'Cliente creado con éxito!!!')
            # Redirigir al login después de crear el cliente
            return redirect('login')

    return render(request, 'registration/Registrar.html', data)

