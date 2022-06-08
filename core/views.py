from django.shortcuts import render
from .models import flores
from .models import macetero
from .models import tierradehoja

# Create your views here.

def home(request):
    
    return render(request, 'core/index.html')

def contacto(request):
    
    return render(request, 'core/contacto.html')

def flores(request):
    flores = flores.objects.all()
    datos ={
        'flores': flores
    }
    return render(request, 'core/flores.html', datos)

def macetero(request):
    macetero = macetero.objects.all()
    datos ={
        'macetero': macetero
    }
    
    return render(request, 'core/macetero.html', datos)

def tierradehoja(request):
    tierradehoja= tierradehoja.objects.all()
    datos ={
        'tierra de hoja': tierradehoja
    }
    
    return render(request, 'core/tierradehoja.html', datos)