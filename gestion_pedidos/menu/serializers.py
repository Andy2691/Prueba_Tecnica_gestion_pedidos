from rest_framework import serializers
from .models import ElementoMenu

class ElementoMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementoMenu
        fields = '__all__'  # Incluye todos los campos del modelo ElementoMenu
