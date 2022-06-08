from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):
    
    return render(request, 'core/index.html')

def contacto(request):
    
    return render(request, 'core/contacto.html')

def flores(request):
    flores = Producto.objects.all()
    datos ={
        'flores': flores
    }
    return render(request, 'core/flores.html', datos)

def macetero(request):
    macetero = Producto.objects.all()
    datos ={
        'macetero': macetero
    }
    
    return render(request, 'core/macetero.html', datos)

def tierradehoja(request):
    tierradehoja= Producto.objects.all()
    datos ={
        'tierra de hoja': tierradehoja
    }
    
    return render(request, 'core/tierradehoja.html', datos)

def flo001(request):
    
    return render(request, 'core/flo001.html')

def flo002(request):
    
    return render(request, 'core/flo002.html')

def flo003(request):
    
    return render(request, 'core/flo003.html')

def flo004(request):
    
    return render(request, 'core/flo004.html')

def mac001(request):
    
    return render(request, 'core/mac001.html')

def mac002(request):
    
    return render(request, 'core/mac002.html')

def mac003(request):
    
    return render(request, 'core/mac003.html')

def mac004(request):
    
    return render(request, 'core/mac004.html')

def tie001(request):
    
    return render(request, 'core/tie001.html')

def tie002(request):
    
    return render(request, 'core/tie002.html')

def tie003(request):
    
    return render(request, 'core/tie003.html')

def tie004(request):
    
    return render(request, 'core/tie004.html')