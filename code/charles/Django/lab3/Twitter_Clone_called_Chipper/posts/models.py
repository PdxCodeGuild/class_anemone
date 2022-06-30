from django.db import models

class Posts(models.Model):
    title = models.TextField(max_length=20)
    author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    body = models.TextField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated_last = models.DateTimeField(add_now=True)
    edited = models.BooleanField()

    def __str__(self):
        return self.title


# Create your models here.
