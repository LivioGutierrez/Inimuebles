from django.shortcuts import render,redirect
from .services import obtener_inmuebles
from .forms import formularioInmueble

# Create your views here.
def index (request):
    inmuebles= obtener_inmuebles
    return render(request,'index.html', {'inmuebles': inmuebles})

def agregar_inmueble(request):
    if request.method == 'POST':
        form = formularioInmueble(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = formularioInmueble()
    
    return render (request, 'agregar_inmueble.html', {'form':form})