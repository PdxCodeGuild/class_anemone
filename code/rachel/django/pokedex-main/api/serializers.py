from rest_framework import serializers
from pokemon.models import Pokemon, Type

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = (
            'type',
            'pokemon',
        )

class PokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(source='Type', many=True, read_only=True)
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
        )