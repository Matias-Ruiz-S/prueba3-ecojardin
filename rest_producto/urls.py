from django.urls import path
from rest_producto.views import lista_productos
from rest_producto import views
from rest_producto.viewslogin import login

urlpatterns = [
    path('lista_productos', lista_productos, name="lista_productos"),
    path('detalle_producto/<id>', views.detalle_producto, name="detalle_producto"),
    path('login', login, name="login"),
]
