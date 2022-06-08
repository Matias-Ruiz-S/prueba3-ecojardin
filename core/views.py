from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm

# Create your views here.

def home(request):
    Productos = Producto.objects.all()
    datos = {
        'producto': Producto
    }
    
    return render(request, 'core/index.html', datos)

def contacto(request):  
    return render(request, 'core/contacto.html')

def flores(request):
    datos = {
        'flores': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/form_producto.html', datos)

def macetero(request):
   datos = {
        'macetero': ProductoForm()
    }
   if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            return render(request, 'core/form_producto.html', datos)


def tierradehoja(request):
   datos = {
        'tierradehoja': ProductoForm()
    }
   if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            return render(request, 'core/form_producto.html', datos)

def form_producto(request):
       datos = {
        'form_producto': ProductoForm()
    }
       if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            return render(request, 'core/form_producto.html', datos)