from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from vehiculo.forms import VehiculoForm

# Create your views here.

# Registrar vehículo
def VenderAuto(request):
    form = VehiculoForm()
    data = {
        'titulo':'Crear Cargo',
        'formulario':form,
        'ruta':'cargos'
    }
    #verificamos si la petición es por método post
    if request.method == 'POST':
        #capturar los datos
        form = VehiculoForm(request.POST)
        print("aaaaaw")
        #verificar si los datos validos, orm de django is_valid()
        if form.is_valid():
            print("aw")
            #save() permtie guardart los datos en la tabla correspondiente
            form.save()
            #messages permite enviar un mensaje al template
            messages.success(request,'Cargado creado con éxito!!!')
            return redirect("homepag")
    return render(request,"cliente/Vender.html", data)  
