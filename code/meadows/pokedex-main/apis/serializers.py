from rest_framework import serializers
from pokemon import models
from django.contrib.auth import get_user_model



class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokemon
        fields = (
            'id',
            'name',
        )

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = (
            'id',
            'type',
        )

class PokemonSerializer(serializers.ModelSerializer):
    type_info = NestedTypeSerializer(many=True, source='types')
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
            'type_info',
        )

class TypeSerializer(serializers.ModelSerializer):
    name_info = NestedPokemonSerializer(many=True, source='pokemon')
    class Meta:
        model = models.Type
        fields = (
            'type',
            'name_info',
            'pokemon',
        )

class UserSerializer(serializers.ModelSerializer):
    caught_info = NestedPokemonSerializer(many=True, read_only=True, source="caught")
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'caught',
            "caught_info",
        )