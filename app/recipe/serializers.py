# serializers for recipe api

from rest_framework import serializers
# from app.core.models import Recipe
# from . import Recipe
from app.core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    # Serializers for recipes

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']