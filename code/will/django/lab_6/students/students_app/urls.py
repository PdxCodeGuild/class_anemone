from django.urls import path

from . import views

app_name = 'students_app'

urlpatterns = [
    path('', views.StudentListView.as_view(), name = 'home'),

]