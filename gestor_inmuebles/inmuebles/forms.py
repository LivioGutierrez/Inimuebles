from django import forms
from .models import Inmueble, Usuario, Tipo_usuario
from django.core.exceptions import ValidationError

class FormularioInmueble(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'm2_cuadraros', 'm2_totales', 'cant_estacionamiento', 'cant_habitacion', 'cant_baño', 'direccion', 'comuna', 'presio_mensual', 'usuario', 'tipo']

class RegistroFormulario(forms.Form):
    rut = forms.CharField(max_length=12, label="RUT")
    nombre = forms.CharField(max_length=50, label="Nombre")
    apellido = forms.CharField(max_length=50, label="Apellido")
    direccion = forms.CharField(max_length=50, label="Dirección")
    telefono_personal = forms.CharField(max_length=12, required=False, label="Teléfono Personal")
    correo_electronico = forms.EmailField(max_length=100, label="Correo Electrónico")
    tipo_usuarios = forms.ModelChoiceField(queryset=Tipo_usuario.objects.all(), label="Tipo de Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        
        if password != password_confirm:
            raise ValidationError("Las contraseñas no coinciden")
        
        return cleaned_data
    
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if Usuario.objects.filter(rut=rut).exists():
            raise ValidationError("El RUT ya está en uso. Por favor, elige otro.")
        return rut

class LoginFormulario(forms.Form):
    rut = forms.CharField(max_length=12, label="RUT")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")