from rest_framework import serializers
from django.contrib.auth import get_user_model
from pokemon.models import Pokemon, Type

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email',)

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'caught', 'username',)

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = (
            'type',
        )

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = (
            'name',
        )

class PokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(source='types', many=True, read_only=True)
    class Meta:
        model = Pokemon
        fields = (
            'id',
            'number',
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'caught_by',
            'type_detail',
        )

class TypeSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(source='pokemon', many=True)
    class Meta:
        model = Type
        fields = (
            'id',
            'type',
            'pokemon_detail',
        )