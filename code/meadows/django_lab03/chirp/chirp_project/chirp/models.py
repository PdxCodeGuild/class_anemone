from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id_user = models.IntegerField(null=True)

    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)

    post_date = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.author.username