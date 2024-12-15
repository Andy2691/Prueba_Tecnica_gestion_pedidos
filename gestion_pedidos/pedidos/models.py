from django.db import models
from usuarios.models import Usuario
from restaurantes.models import Restaurante
from menu.models import ElementoMenu

class Pedido(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ])
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    direccion_entrega = models.TextField()
    instrucciones_especiales = models.TextField(null=True, blank=True)
    tiempo_estimado_entrega = models.DateTimeField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    elemento_menu = models.ForeignKey(ElementoMenu, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    notas = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Detalle {self.id} del Pedido {self.pedido.id}"
