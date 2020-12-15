from rest_framework import serializers
from core.models import Recipe
from django.contrib.auth.hashers import make_password


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['recipe_name', 'description', 'image']
