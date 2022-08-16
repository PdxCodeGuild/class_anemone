from rest_framework import serializers
from django.contrib.auth import get_user_model
from pokemon.models import Pokemon, Type

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('type')

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('name')


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by')
        

class TypeSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer
    class Meta:
        model = Type 
        fields = ('id', 'type', 'pokemon')

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'caught', 'username')