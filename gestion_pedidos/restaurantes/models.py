from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    calificacion = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')])
    categoria = models.CharField(max_length=100)
    latitud = models.DecimalField(max_digits=13, decimal_places=11)
    longitud = models.DecimalField(max_digits=13, decimal_places=11)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
