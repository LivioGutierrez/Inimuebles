from django.contrib import admin
from .models import Tipo_usuario,Region,Comuna,Usuario,Inmueble,Estado_inmueble,Tipo_inmueble

# Register your models here.
admin.site.register(Tipo_usuario)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Usuario)
admin.site.register(Inmueble)
admin.site.register(Estado_inmueble)
admin.site.register(Tipo_inmueble)