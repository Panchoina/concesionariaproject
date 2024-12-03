from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from empleado.forms import EmpleadoForm
from empleado.models import Empleado
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

# login de los empleados
def inicio(request):
    return render(request,'Index.html')
# Los empleados seran registrados por la pagina de forma administrativa

# CRUD
# registro de empleado
@permission_required(['empleado.add_empleado'], login_url='/accounts/login/', raise_exception=True)
def RegistroEmpleado(request):
    form = EmpleadoForm()
    data = {
        'titulo': 'Crear Empleado',
        'formulario': form,
    }

    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():

            # Obtener datos del formulario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # Crear el usuario de Django
            user = User.objects.create_user(username=username, password=password)

            # Crear el empleado asociado
            empleado = form.save(commit=False)
            empleado.user = user  # Asociamos el empleado con el usuario
            empleado.save()

            # Asignar al grupo "Empleados" y darle permisos si es necesario
            grupo_empleados, created = Group.objects.get_or_create(name='Empleados')
            user.groups.add(grupo_empleados)

            # Autenticar al usuario automáticamente
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Empleado creado con éxito!!!')
                return redirect('homepag')  # Redirige al login u otra página según corresponda
            else:
                messages.error(request, 'Hubo un error al registrarse')
        else:
            data['formulario'] = form

    return render(request, 'registration/agregarEmpleado.html', data)

# Lista de los empleados

@permission_required(['empleado.view_empleado'], login_url='/accounts/login/', raise_exception=True)
def listar(request):
    deptos = Empleado.objects.all()
    data = {'lista':deptos}
    return render(request,'empleado/verempleados.html',data)

@permission_required(['empleado.delete_empleado'], login_url='/accounts/login/', raise_exception=True)
def EliminarEmpleado(request,id):
    item = Empleado.objects.get(pk=id)
    item.delete()
    return redirect('listar')

@permission_required(['empleado.change_empleado'], login_url='/accounts/login/', raise_exception=True)
def ActualizarEmpleado(request,id):
    # aqui se busca el empleado por la id que le damos por el boton
    item = Empleado.objects.get(pk=id)
    form = EmpleadoForm(instance=item)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,'Empleado editado con éxito')
    data = {
        'titulo':'Editar Empleado',
        'formulario':form,
        'ruta':'empleados'
    }
    return render(request,'registration/agregarEmpleado.html',data)

# Imprimir los empleados a excel
def ImprimirEmpleados(request):
    return render(request,"")