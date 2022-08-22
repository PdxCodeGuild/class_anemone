from django.db import models

class Post(models.Model):
    author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    content_text = models.CharField(max_length=140)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.author)

    class Meta:
        ordering = ['-create_date']