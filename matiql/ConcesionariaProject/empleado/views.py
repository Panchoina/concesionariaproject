from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from empleado.forms import EmpleadoFiltro, EmpleadoForm
from empleado.models import Empleado
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import xlwt
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
    empleados = Empleado.objects.all()  # Obtenemos todos los empleados inicialmente
    filtro = EmpleadoFiltro(request.GET) 
    # Si el formulario es válido, aplicamos los filtros
    if filtro.is_valid():
        area = filtro.cleaned_data.get('area')

        # Filtrar según el área seleccionada
        if area:
            empleados = empleados.filter(area=area)
    data = {'lista':empleados}
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
def ImportarEmpleados(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Empleados'] = 'attachment; filename=empleados.xls'
    archivo = xlwt.Workbook(encoding='utf-8')
    hoja = archivo.add_sheet('Empleados')

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columnas = ['Run','Nombre','Apellido','Dirección','Fono de el Empleado','gmail','area','contraseña','Fecha Nacimiento','user_id']

    for i in range(len(columnas)):
        hoja.write(row_num,i,columnas[i],font_style)

    font_style = xlwt.XFStyle()
    filas = Empleado.objects.all().values_list('rut','nombre','apellido','direccion','FonoEmpleado','gmail','area','contraseña','FechaNacimiento','user_id')
    for f in filas:
        row_num += 1
        for i in range(len(f)):
            hoja.write(row_num,i,f[i],font_style)
    #guardar el archivo
    archivo.save(response)
    return response