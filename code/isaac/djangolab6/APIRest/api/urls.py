from django.urls import path, include 
from rest_framework.routers import DefaultRouter

from . import views 

router = DefaultRouter()
router.register('student', views.StudentViewSet, basename='student')


urlpatterns = router.urls 


# urlpatterns = [ 
#     path('', include(router.urls)),
#     path('student/', views.StudentDetail.as_view()),
# ]