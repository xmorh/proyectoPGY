from django.db import models
from django.db.models.base import ModelBase
from django.db.models.deletion import CASCADE, PROTECT

# Definición de material, para diferentes tipos de productos textiles 
class Material(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre_cate = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_cate

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fecha_ingreso = models.DateField(auto_now=True)
    dimensiones = models.CharField(max_length=15)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    f_nacimiento = models.DateField()
    comuna = models.CharField(max_length=20)
    producto = models.ForeignKey(Producto, on_delete=CASCADE)

    def __str__(self):
        return self.nombre
       
opciones_mensaje = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_mensaje = models.IntegerField(choices=opciones_mensaje)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre