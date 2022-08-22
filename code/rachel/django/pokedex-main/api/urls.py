from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pokemon', views.PokemonViewSet, basename='pokemon')
router.register('type', views.TypeViewSet, basename='type')
router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('currentuser/', views.CurrentUserView.as_view()), 
]
