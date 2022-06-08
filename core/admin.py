from django.contrib import admin
from .models import Categoria, flores, macetero, tierradehoja

# Register your models here.

admin.site.register(Categoria)
admin.site.register(flores)
admin.site.register(macetero)
admin.site.register(tierradehoja)
