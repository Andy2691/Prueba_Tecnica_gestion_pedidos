from django.db import models
from restaurantes.models import Restaurante

class ElementoMenu(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_preparacion = models.IntegerField()  # en minutos
    disponible = models.BooleanField(default=True)
    categoria = models.CharField(max_length=100)
    url_imagen = models.URLField(max_length=255, null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
