from unicodedata import name
from django.urls import path
from .views import home, macetero
from .views import contacto
from .views import flores
from .views import macetero
from .views import tierradehoja
from .views import form_producto

urlpatterns = [
    path('', home,name="home"),
    path('contacto.html', contacto,name="contacto"),
    path('flores.html', flores,name="flores"),
    path('macetero.html', macetero,name="macetero"),
    path('tierradehoja.html', tierradehoja,name="tierradehoja"),
    path('form_producto.html', form_producto, name='form_producto'),
]
