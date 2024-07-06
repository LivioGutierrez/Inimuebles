from django.db import models

class Tipo_usuario(models.Model):
    nombre=models.CharField(max_length= 50, null= False)

class Usuario (models.Model):
    rut = models.CharField(max_length=12, null=False, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=50, null=False)
    telefono_personal = models.CharField(max_length=12, null=True)
    correo_electronico = models.CharField(max_length=100, null=False)
    tipo_usuarios= models.OneToOneField(Tipo_usuario, null=False, on_delete=models.CASCADE)

class Inmueble(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=500, null=False)
    m2_cuadraros = models.IntegerField(null=False)
    m2_totales = models.IntegerField(null=False)
    cant_estacionamiento = models.IntegerField(null=False)
    cant_habitacion = models.IntegerField(null=False)
    cant_baño = models.IntegerField(null=False)
    direccion = models.CharField(max_length=50, null=False)
    comuna = models.CharField(max_length=200, null=False)
    tipo_inmueble = models.CharField(max_length=40, null=False)
    presio_mensual = models.FloatField(null=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Estado_inmueble(models.Model):
    activo = models.BooleanField(null=False, default=False)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    inmueble = models.OneToOneField(Inmueble, null= False)

class Region(models.Model):
    nombre = models.CharField(max_length=50, null= False)
    region = models.ForeignKey(Inmueble, on_delete=models.CASCADE)

class Comuna(models.Model):
    nombre = models.CharField(max_length=50, null= False)
    comuna = models.ForeignKey(Inmueble, on_delete=models.CASCADE)

class Tipo_inmueble(models.Model):
    nombre = models.CharField(max_length=50, null= False)
    region = models.ForeignKey(null=False, on_delete=models.CASCADE)