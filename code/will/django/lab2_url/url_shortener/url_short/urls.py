from django.urls import path

from . import views

app_name = 'url_shortener'
urlpatterns = [
  
    path('', views.index, name='index'),
    path('url', views.url, name="url"),
    path('slug', views.slug, name='slug'),
]