from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [ 
    path('', views.ChirpListView.as_view(), name='home'),
    ## not sure if post/int:pk will work for this one since i am trying to show the users page with
    ## all of their chirps
    ## may need to replace with string username or something
    path('post/<int:pk>', views.UserView.as_view(), name='detail'),
    path('post/<int:pk>/edit/', views.ChirpEditView.as_view(), name='edit'),
    path('post/<int:pk>/delete/', views.ChirpDeleteView.as_view, name='delete'),
]