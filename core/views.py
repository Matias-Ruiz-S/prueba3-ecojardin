from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'core/index.html')

def contacto(request):
    
    return render(request, 'core/contacto.html')

def flores(request):
    
    return render(request, 'core/flores.html')

def macetero(request):
    
    return render(request, 'core/macetero.html')

def tierradehoja(request):
    
    return render(request, 'core/tierradehoja.html')