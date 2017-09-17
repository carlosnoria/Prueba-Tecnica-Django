"""
Prueba Tecnica Kronos
Autor: Carlos Noria

Los serializadores se implementaron partiendo de los 'ModelSerializers'
para ahorrar tiempo de codificacion y permitirle a la API REST trabajar
bajo la maxima optimizacion que garantiza rest_framework.
"""

from rest_framework import serializers
from kronos_rest.models import Ciudad, Tienda, Usuario

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id', 'name')

class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = ('id', 'name', 'city', 'users')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'name', 'last_name', 'document')

