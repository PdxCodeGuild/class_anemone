from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [ 
    path('', views.ChirpListView.as_view(), name='home'),
    ## not sure if post/int:pk will work for this one since i am trying to show the users page with
    ## all of their chirps

    # path('post/<int:pk>/', views.ChirpDetailView.as_view(), name='detail'),
    path('post/<int:pk>/delete/', views.ChirpDeleteView.as_view(), name='delete'),
]