from rest_framework import serializers
from django.contrib.auth import get_user_model
from pokemon.models import Pokemon, Type
from users.models import CustomUser

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'caught_by')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class PokemonSerializer(serializers.ModelSerializer):
    user_detail = NestedUserSerializer(read_only=True, source='username')
    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by', 'user_detail')

class UserSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(many=True, source='name', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'pokemon_detail')