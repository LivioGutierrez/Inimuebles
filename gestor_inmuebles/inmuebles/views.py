from django.shortcuts import render,redirect
from .services import obtener_inmuebles
from .forms import FormularioInmueble, RegistroFormulario, LoginFormulario
from .models import Usuario
from django.views import View
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages

# Create your views here.
def index (request):
    inmuebles= obtener_inmuebles
    return render(request,'index.html', {'inmuebles': inmuebles})

def agregar_inmueble(request):
    if request.method == 'POST':
        form_inmuebles = FormularioInmueble(request.POST)
        if form_inmuebles.is_valid():
            form_inmuebles.save()
            return redirect('index')
    else:
        form_inmuebles = FormularioInmueble()
    
    return render (request, 'agregar_inmueble.html', {'form':form_inmuebles})

class RegistroView(View):
    def get(self, request):
        form = RegistroFormulario()
        return render(request, 'registration/register.html', {'form': form})
    
    def post(self, request):
        form = RegistroFormulario(request.POST)
        
        if form.is_valid():
            rut = form.cleaned_data['rut']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            direccion = form.cleaned_data['direccion']
            telefono_personal = form.cleaned_data['telefono_personal']
            correo_electronico = form.cleaned_data['correo_electronico']
            tipo_usuarios = form.cleaned_data['tipo_usuarios']
            password = form.cleaned_data['password']
            
            # Crear el usuario
            UserModel = get_user_model()
            user = UserModel.objects.create_user(username=rut, password=password, email=correo_electronico)
            
            # Crear el objeto Usuario
            usuario = Usuario.objects.create(
                rut=rut,
                nombre=nombre,
                apellido=apellido,
                direccion=direccion,
                telefono_personal=telefono_personal,
                correo_electronico=correo_electronico,
                tipo_usuarios=tipo_usuarios,
                # user=user
            )
            
            return redirect('index')
        
        return render(request, 'registration/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginFormulario()
        return render(request, 'registration/login.html', {'form': form})
    
    def post(self, request):
        form = LoginFormulario(request.POST)
        
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data['password']
            print(f" {rut} - {password}")
            
            # Autenticar el usuario
            user = authenticate(request, rut=rut, password=password)
            if user is not None:
                print(f"el rut: {rut} y la contraseña: {password} no existe")
                login(request, user)
                return redirect('index.html')
            else:
                messages.error(request, "RUT o contraseña incorrectos")
                
            return redirect('index')
        return render(request, 'registration/login.html', {'form': form})