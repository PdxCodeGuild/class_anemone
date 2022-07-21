from rest_framework import serializers
from pokemon.models import Pokemon, Type


class ClassSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('__all__')



class PokemonSerlializer(serializers.ModelSerializer):
    types = ClassSerlializer(many=True)
    class Meta:
        model = Pokemon
        fields = (
            'number',
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'caught_by',
            'types',
            )

