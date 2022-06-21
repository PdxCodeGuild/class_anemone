from django.urls import path
from .views import home_page_view, url_short

urlpatterns = [
    path('', home_page_view, name='home'),
    path('urlshort', url_short, name='url'),
]
