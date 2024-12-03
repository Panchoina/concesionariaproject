from django import forms
from cliente.models import Cliente

class ClienteFormRegis(forms.ModelForm):
    password_cliente = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'apellido', 'direccion', 'FonoCliente', 'gmail', 'FechaNacimiento']
        widgets = {
            'rut': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'FonoCliente': forms.NumberInput(attrs={'class': 'form-control'}),
            'gmail': forms.EmailInput(attrs={'class': 'form-control'}),
            'FechaNacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password_cliente')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data
