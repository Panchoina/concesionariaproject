from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Empleado
        fields = ['rut', 'nombre', 'apellido', 'direccion', 'FonoEmpleado', 'gmail', 'area', 'FechaNacimiento']
        widgets = {
            'rut': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'FonoEmpleado': forms.NumberInput(attrs={'class': 'form-control'}),
            'gmail': forms.EmailInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'FechaNacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2
