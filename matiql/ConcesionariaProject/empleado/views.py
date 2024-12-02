from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from empleado.forms import EmpleadoForm

# Create your views here.

# login de los empleados
@login_required(login_url='accounts/login')
def inicio(request):
    return render(request,'Index.html')
# Los empleados seran registrados por la pagina de forma administrativa

# CRUD

# registro de empleado
@permission_required('empleado.add_empleado',login_url='/')
def CrearEmpleado(request):
    form = EmpleadoForm()
    data = {
        'titulo':'Crear Cargo',
        'formulario':form,
        'ruta':'cargos'
    }
    # verificamos si el form es post
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        # verificacion si es valido los datos que entregamos por el fomulario de html
        if form.is_valid():
            # aqui guardamos los datos con esta funcion
            form.save()
            #messages permite enviar un mensaje al template
            messages.success(request,'Cargado creado con éxito!!!')
    return render(request,'empleado/agregarEmpleado.html',data)

# Lista de los empleados
@permission_required('empleado.view_empleado',login_url='/')
def ListarEmpelados(request):
    deptos = Empleado.objects.all()
    data = {'lista':deptos}
    return render(request,'empleado/empleados.html',data)

# editar empleados
def ActualizarEmpleados(request,id):
    #buscar el cargo por su id
    item = Empleado.objects.get(pk=id)
    #item que contiene el Empleado buscado
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
    return render(request,'empleado/create.html',data)

# Imprimir los empleados a excel
def ImprimirEmpleados(request):
    return render(request,"")