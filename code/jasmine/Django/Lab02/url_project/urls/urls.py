from django.urls import path
from . import views

app_name = 'urls'

# Create your views here.
urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/<str:short_url>', views.redirect, name='redirect')

]