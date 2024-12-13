from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'nombre', 'año', 'actores_principales', 'resumen', 'imagen_url']
