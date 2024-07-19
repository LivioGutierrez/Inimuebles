from django import forms
from .models import Inmueble

class formularioInmueble(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['nombre', 'descripcion', 'm2_cuadraros', 'm2_totales', 'cant_estacionamiento', 'cant_habitacion', 'cant_baño', 'direccion', 'comuna', 'presio_mensual', 'tipo']