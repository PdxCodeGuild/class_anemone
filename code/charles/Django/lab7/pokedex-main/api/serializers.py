from rest_framework import serializers
from django.contrib.auth import get_user_model
from pokemon.models import Pokemon, Type
from users.models import CustomUser

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('name',)

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('type',)

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class PokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(many=True, read_only=True, source='types')
    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'height', 'type_detail', 'weight', 'image_front', 'image_back', 'caught_by',)

class TypeSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(many=True, source='pokemon', read_only=True)
    class Meta:
        model = Type
        fields = ('type', 'pokemon_detail')

class UserSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(many=True, source='name', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'pokemon_detail')