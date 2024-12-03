from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.template import RequestContext
from cliente.forms import ClienteFormRegis
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from vehiculo.models import Vehiculo
from django.contrib.auth.models import Group, Permission

# Vista de inicio, redirige si no está autenticado
@login_required(login_url='accounts/login')
def inicio(request):
    return render(request, 'Index.html',context=RequestContext(request))

# Vista para la página principal de los clientes, con permisos
#@permission_required(['cliente.view_cliente'], login_url='/accounts/login/', raise_exception=True)
def homepag(request):
    # lista de los vehiculos en venta
    
    vehiculos = Vehiculo.objects.all()
    data = {'lista':vehiculos}
    return render(request, "cliente/Inicio.html", data)

# Registro de un cliente
def Registro(request):
    form = ClienteFormRegis()
    data = {
        'titulo': 'Crear Cliente',
        'formulario': form,
    }
    if request.method == 'POST':
        form = ClienteFormRegis(request.POST)
        if form.is_valid():
            # Obtener datos del formulario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password_cliente']
            # Crear el usuario de Django
            user = User.objects.create_user(username=username, password=password)
            # Crear el cliente asociado
            cliente = form.save(commit=False)
            cliente.user = user  # Asociamos el cliente con el usuario
            cliente.save()
            # Asignar el cliente al grupo "Clientes"
            grupo_clientes, created = Group.objects.get_or_create(name='Clientes')
            user.groups.add(grupo_clientes)
            # Autenticar al usuario automáticamente
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Cliente creado con éxito!!!')
                return redirect('login')
            else:
                messages.error(request, 'Hubo un error al registrarse')
        else:
            data['formulario'] = form
    return render(request, 'registration/Registrar.html', data)