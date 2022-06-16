from django.urls import path

from . import views

app_name = 'choppa'

urlpatterns = [
    path('', views.index, name='index'),
    path('url_chop/', views.url_chop, name='url_chop'),
    path('remove/', views.remove, name='remove'),

]