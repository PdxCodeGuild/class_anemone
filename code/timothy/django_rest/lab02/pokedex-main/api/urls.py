from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('pokemon', views.PokemonViewSet, basename='pokemon')

urlpatterns = router.urls 