from django.db import models
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=150)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.pk,))

    class Meta:
        ordering = ['-created']
