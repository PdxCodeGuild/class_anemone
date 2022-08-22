from django.db import models
from django.views.generic import TemplateView

# Create your models here.
class PostView(TemplateView):
    post_name = "home.html"