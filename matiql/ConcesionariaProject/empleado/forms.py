from django import forms

from empleado.models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        # model que sale desde models.py que es donde se guardaran los datos
        model = Empleado
        fields =['rut','nombre','apellido','direccion','FonoEmpleado','gmail','area','contraseña','FechaNacimiento']
        widgets = {
            'rut':forms.NumberInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'FonoEmpleado':forms.NumberInput(attrs={'class':'form-control'}),
            'gmail':forms.TextInput(attrs={'class':'form-control'}),
            'area':forms.TextInput(attrs={'class':'form-select'}),
            'contraseña':forms.TextInput(attrs={'class':'form-select'}),
            'FechaNacimiento':forms.TextInput(attrs={'class':'form-select','type':'date'}),
        }