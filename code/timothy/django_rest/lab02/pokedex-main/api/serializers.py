from rest_framework import serializers
from pokemon import models



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