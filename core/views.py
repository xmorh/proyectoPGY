from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def banderines(request):
    return render(request, 'banderines.html')

def scrunchies(request):
    return render(request, 'scrunchies.html')

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
    return render(request, 'contacto.html')
