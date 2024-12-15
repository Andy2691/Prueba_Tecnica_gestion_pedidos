from django.contrib import admin
from .models import Reporte

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_generacion', 'estado')
    list_filter = ('estado', 'fecha_generacion')
    search_fields = ('nombre',)
