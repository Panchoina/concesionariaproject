from django import forms
from cliente.models import Cliente

class ClienteFormRegis(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'apellido', 'direccion', 'FonoCliente', 'gmail', 'password_cliente', 'FechaNacimiento']
        widgets = {
            'rut': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'FonoCliente': forms.NumberInput(attrs={'class': 'form-control'}),
            'gmail': forms.EmailInput(attrs={'class': 'form-control'}),
            'password_cliente': forms.PasswordInput(attrs={'class': 'form-control'}),  # Campo para la contraseña
            'FechaNacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
