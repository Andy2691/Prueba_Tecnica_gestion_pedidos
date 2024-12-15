from django.db import models

class Reporte(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=50,
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_proceso', 'En Proceso'),
            ('completado', 'Completado'),
        ]
    )
    archivo = models.FileField(upload_to='reportes/', null=True, blank=True)

    def __str__(self):
        return self.nombre
