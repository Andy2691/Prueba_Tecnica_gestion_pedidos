from django.db import models
from restaurantes.models import Restaurante

class Usuario(models.Model):
    TIPOS = [
        ('cliente', 'Cliente'),
        ('distribuidor', 'Distribuidor'),
    ]

    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True, blank=True)
    primer_nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion_predeterminada = models.TextField(null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.primer_nombre} {self.apellido}"
