from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('pokemon', views.PokemonViewSet, basename='pokemon')
router.register('users', views.UserViewSet, basename='users')
router.register('type', views.TypeViewSet, basename='type')
urlpatterns = router.urls + [
    path('<int:pk>/', views.PokemonDetail.as_view()),
]