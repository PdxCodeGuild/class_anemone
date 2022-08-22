from rest_framework import serializers

from pokemon.models import Pokemon, Type
from users.models import CustomUser

# class NestedUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('username')

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('type',)

class NestedPokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = ('name',)

class PokemonSerializer(serializers.ModelSerializer):
    # user_detail = NestedUserSerializer(many=True, source='username', read_only=True)
    type_detail = NestedTypeSerializer(many=True, source='types', read_only=True)
  
    class Meta:
        model = Pokemon
        fields = ('id', 'number', 'type_detail', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('caught', 'id', 'username')

class TypeSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(many=True, source='pokemon', read_only=True)
    class Meta:
        model = Type
        fields = ('pokemon_detail', 'type')