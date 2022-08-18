from rest_framework import serializers

from pokemon.models import Pokemon, Type

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('name',)

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('type',)


class PokemonSerializer(serializers.ModelSerializer):
    type_info = NestedTypeSerializer(many=True, source='types', read_only=True)
    class Meta:
        model = Pokemon
        fields = ('id', 'number', 'name', 'height', 'weight', 'image_front', 'image_back', 'type_info')


class TypeSerializer(serializers.ModelSerializer):
    pokemon_info = NestedPokemonSerializer(many=True, source='pokemon', read_only=True)
    class Meta:
        model = Type
        fields = ('id', 'type', 'pokemon_info')