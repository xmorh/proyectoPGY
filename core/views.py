from django.core.exceptions import ImproperlyConfigured
from core.models import Producto
from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def banderines(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'banderines.html', data)



def scrunchies(request):
    productos = Producto.object.all()
    data = {
        'productos' : productos
    }
    return render(request, 'scrunchies.html', data)



def catalogo(request):
    return render(request, 'catalogo.html')

def clientes(request):
    return render(request, 'clientes.html')

def ofertas(request):
    return render(request, 'ofertas.html')

def usuario(request):
    return render(request, 'usuario.html')

def registro(request):
    return render(request, 'registro.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "¡Mensaje enviado!"
        else:
            data["form"] = formulario

    return render(request, 'contacto.html', data)
   