from django.db import models
from django.urls import reverse



class witter_app(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='witter_app')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=255)


    def __str___(self):
        return self.title
