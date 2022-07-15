from rest_framework import serializers
from pokemon import models



class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
        )
        model = models.Pokemon

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'type',
        )
        model = models.Type

class PokemonSerializer(serializers.ModelSerializer):
    type = NestedTypeSerializer(many=True, source='type')
    class Meta:
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
        model = models.Pokemon

class TypeSerializer(serializers.ModelSerializer):
    name = NestedPokemonSerializer(many=True, source='pokemon')
    class Meta:
        fields = (
            'type',
            'name',
            'pokemon',
        )
        model = models.Type