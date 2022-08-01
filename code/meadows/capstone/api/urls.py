from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('blog', views.BlogViewSet, basename='blog')
router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('<int:pk>', views.BlogDetailView.as_view()),
    path('currentuser/', views.CurrentUserView.as_view())
]
