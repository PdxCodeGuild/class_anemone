from rest_framework import serializers
from pokemon import models
# from users.models import CustomUser
from django.contrib.auth import get_user_model


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
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

        model = models.Pokemon

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'caught',
            'id',
            'username',

        )
        model = get_user_model()
