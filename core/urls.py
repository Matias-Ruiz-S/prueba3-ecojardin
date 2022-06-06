from django.urls import path
from .views import home, macetero
from .views import contacto
from .views import flores
from .views import macetero
from .views import tierradehoja

urlpatterns = [
    path('', home,name="home"),
    path('contacto.html', contacto,name="contacto"),
    path('flores.html', flores,name="flores"),
    path('macetero.html', macetero,name="macetero"),
    path('tierradehoja.html', tierradehoja,name="tierradehoja"),
]
