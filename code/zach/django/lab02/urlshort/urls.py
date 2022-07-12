from django.urls import path
from .views import home_page_view, url_short, url_Redirect
app_name = 'url_shortener'
urlpatterns = [
    path('', home_page_view, name='home'),
    path('urlshort', url_short, name='url'),
    path('<str:slug>/', url_Redirect, name='redirect')
]
