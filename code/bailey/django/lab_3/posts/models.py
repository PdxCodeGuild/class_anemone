from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.pk,))

    class Meta:
        ordering = ['-created']



class Comments(models.Model):
    CommentPost = models.ForeignKey(Post , on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')

    class Meta:
        ordering=['-date_posted']

    def __str__(self):
        return str(self.author) + ' comment ' + str(self.content)

    @property
    def children(self):
        return Comments.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
    