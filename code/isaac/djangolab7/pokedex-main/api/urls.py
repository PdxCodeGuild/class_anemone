from django.urls import path 
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('pokemon', views.PokemonView, basename='pokemon')
router.register('type', views.TypeView, basename='type')
router.register('users', views.UserView, basename='users')


urlpatterns = router.urls + [
    path('currentuser/', views.CurrentUser.as_view()),
]