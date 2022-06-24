from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    post_date = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        return self.title
