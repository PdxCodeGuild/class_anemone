from rest_framework import serializers
from pokemon import models
from django.contrib.auth import get_user_model



class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokemon
        fields = (
            'name',
        )

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = (
            'type',
        )

class PokemonSerializer(serializers.ModelSerializer):
    type = NestedTypeSerializer(many=True, source='types')
    class Meta:
        model = models.Pokemon
        fields = (
            'id',
            'number',
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'caught_by',
            'type',
        )

class TypeSerializer(serializers.ModelSerializer):
    name = NestedPokemonSerializer(many=True, source='pokemon')
    class Meta:
        model = models.Type
        fields = (
            'type',
            'name',
            'pokemon',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'caught'
        )