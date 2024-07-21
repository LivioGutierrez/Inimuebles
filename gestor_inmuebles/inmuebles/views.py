from django.shortcuts import render,redirect
from .services import obtener_inmuebles
from .forms import FormularioInmueble, FormularioRegistro, UsuarioForm
from django.views import View
from django.contrib.auth import login

# Create your views here.
def index (request):
    inmuebles= obtener_inmuebles
    return render(request,'index.html', {'inmuebles': inmuebles})

def agregar_inmueble(request):
    if request.method == 'POST':
        form = FormularioInmueble(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FormularioInmueble()
    
    return render (request, 'agregar_inmueble.html', {'form':form})

class RegistroView(View):
    def get(self, request):
        user_form = FormularioRegistro()
        usuario_form = UsuarioForm()
        return render(request,'registration/register.html', {'user_form': user_form, 'usuario_form': usuario_form})
    
    def post(self, request):
        user_form = FormularioRegistro(request.POST)
        usuario_form = UsuarioForm(request.POST)
        
        if user_form.is_valid() and usuario_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            usuario = usuario_form.save(commit=False)
            usuario.user = user
            usuario.save()
            
            login(request, user)
            return redirect('index')
        return render(request, 'registration/register.html', {'user_form': user_form, 'usuario_form': usuario_form})