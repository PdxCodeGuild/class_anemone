from django.urls import path
from rest_framework import routers
from .views import CurrentUserView
from . import views

router = routers.SimpleRouter()

router.register('pokemon', views.PokemonViewSet, basename = 'pokemon')



urlpatterns = [
  


    path('current-user/', CurrentUserView.as_view()),
    


]

urlpatterns += router.urls