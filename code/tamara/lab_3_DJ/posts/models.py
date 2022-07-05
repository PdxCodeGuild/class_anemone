from django.db import models
from django.urls import reverse

class Post(models.Model):
    # makes sure the author is the logged in user and assigns them to the author variable 
    author = models.CharField(max_length=10)
        ####### ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=123)

    def __str__(self):
        return self.body
        # shows the chirp body as the name of the item in the admin panel
    
    ####### def get_absolute_url(self):
    #     return reverse('posts:detail', args=(self.pk,))
    #     ##### will automatically reverse the url when submitting a form on the detail url

    # will order from newest to oldest chirps
    class Meta:
        ordering = ['-created']
