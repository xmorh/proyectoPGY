from django.contrib import admin
from .models import Categoria, Material, Producto, Cliente
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_ingreso', 'dimensiones', 'material']
    list_editable = ['nombre']
    search_fields = ['material']
    list_per_page = 15

admin.site.register(Material)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Categoria)