from django.urls import path

from . import views

app_name='posts'

urlpatterns=[
    path('',views.TwiddleListView.as_view(), name = 'landing'),
    path('twiddle/<int:pk>/detail',views.TwiddleDetailView.as_view(),name = 'detail'),
    path('twiddle/create', views.TwiddleCreateView.as_view(), name = 'create'),
    path('twiddle/<int:pk>/edit/', views.TwiddleEditView.as_view(),name ='edit'),
    path('twiddle/<int:pk>/delete/', views.TwiddleDeleteView.as_view(), name ='delete')
]