from django.db import models
from django.db.models.base import ModelBase
from django.db.models.deletion import CASCADE, PROTECT

# Create your models here

# Definición de material, para diferentes tipos de productos textiles 
class Material(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    fecha_ingreso = models.DateField(auto_now=True)
    dimensiones = models.CharField(max_length=15)
    material = models.ForeignKey(Material, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to='media', null=True)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    f_nacimiento = models.DateField()
    comuna = models.CharField(max_length=20)
    producto = models.ForeignKey(Producto, on_delete=CASCADE)

    def __str__(self):
        return self.nombre