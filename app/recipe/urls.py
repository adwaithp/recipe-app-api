# urls mapping for recipe App

from django.urls import path,include

from rest_framework.routers import DefaultRouter
from . import views
# from app.recipe import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewset)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]