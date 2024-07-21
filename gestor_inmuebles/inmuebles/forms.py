from django import forms
from django.contrib.auth.models import User
from .models import Inmueble, Usuario

class FormularioInmueble(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'm2_cuadraros', 'm2_totales', 'cant_estacionamiento', 'cant_habitacion', 'cant_baño', 'direccion', 'comuna', 'presio_mensual', 'tipo']

class FormularioRegistro(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")
    
    class Meta:
        model = User
        # fields = ['username', 'email', 'password']
        fields = ['password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut', 'nombre', 'apellido', 'direccion', 'telefono_personal', 'correo_electronico', 'correo_electronico', 'tipo_usuarios']
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'apellido':'Apellido',
            'direccion':'Direccion',
            'telefono_personal':'Telefono Personal',
            'tipo_usuarios':'Tipo de Usuario',
        }