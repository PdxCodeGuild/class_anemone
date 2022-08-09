from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.TextField(max_length=50)
    author = models.ForeignKey('auth.user', related_name="posts", on_delete=models.CASCADE)
    body = models.TextField(max_length=128)
    created = models.DateTimeField(auto_now_add = True)
    updated_last = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", args=(self.pk,))

    class Meta:
        ordering = ['-created']
    


# Create your models here.
