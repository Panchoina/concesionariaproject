from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from empleado.forms import EmpleadoForm
from empleado.models import Empleado
# Create your views here.

# login de los empleados
def inicio(request):
    return render(request,'Index.html')
# Los empleados seran registrados por la pagina de forma administrativa

# CRUD
# registro de empleado
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
def listar(request):
    deptos = Empleado.objects.all()
    data = {'lista':deptos}
    return render(request,'empleado/verempleados.html',data)

def EliminarEmpleado(request,id):
    item = Empleado.objects.get(pk=id)
    item.delete()
    return redirect('listar')

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
    return render(request,'empleado/agregarEmpleado.html',data)

# Imprimir los empleados a excel
def ImprimirEmpleados(request):
    return render(request,"")