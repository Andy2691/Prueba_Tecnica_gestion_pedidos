from rest_framework import serializers
from .models import Restaurante

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'  # Incluye todos los campos del modelo Restaurante
