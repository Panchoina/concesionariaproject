from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['descripcion', 'marca', 'modelo', 'año', 'precio', 'propietario']  # Corregido: 'fields = fields = ...'
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'propietario': forms.Select(attrs={'class': 'form-control'}),
        }

