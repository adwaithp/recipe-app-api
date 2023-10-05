# views for recipe APIs

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializers
from ..core.models import Recipe


class RecipeViewset(viewsets.ModelViewSet):
    # view for manage recipe APIs
    serializers_class =  serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrive recipes for authenticated user
        return self.queryset.filter(user=self.request.user).order_by('-id')
