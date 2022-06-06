from django.urls import path
from .views import home, macetero
from .views import contacto
from .views import flores
from .views import macetero
from .views import tierradehoja

urlpatterns = [
    path('', home,name="home"),
    path('', contacto,name="contacto"),
    path('', flores,name="flores"),
    path('', macetero,name="macetero"),
    path('', tierradehoja,name="tierradehoja"),
]
