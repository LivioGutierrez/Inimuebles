from .models import Tipo_usuario, Usuario, Inmueble, Estado_inmueble, Region, Comuna, Tipo_inmueble

def obtener_inmuebles():
    return Inmueble.objects.all()

