from django.urls import path
from . import views

app_name = 'grocerylist_app' # for namespacing
urlpatterns = [
    path(' ', views.index, name='index')
]