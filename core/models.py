from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')


def __str__(self):
    return self.nombreCategoria


class Producto(models.Model):
    SKU = models.CharField(max_length=12, primary_key=True, verbose_name='SKU')
    Nombredelproducto = models.CharField(max_length=20, verbose_name='Nombre del producto')
    Precio = models.CharField(max_length=20, verbose_name='Precio')
    Stock = models.CharField(max_length=20, null=True, blank=True, verbose_name='Stock disponible')
    CategoriaId = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    

    

    