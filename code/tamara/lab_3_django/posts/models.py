from django.db import models
from django.urls import reverse

class Post(models.Model):
    # thus author is linked to a foreignkey so they have a unique identifier
    # if the user is deleted then it will CASCADE
    author = models.ForeignKey('auth.User', related_name="posts", on_delete=models.CASCADE)
    # author = models.CharField(max_length=20, unique=True)
    # created date will automatically be now
    created = models.DateTimeField(auto_now_add=True)
    # body is the text of the chirp
    body = models.CharField(max_length=128)

    def __str__(self):
        return self.body
        # will show the username of the person who made the chirp in the admin panel
    
    #### BELOW Not working for redirecting after creating new Chirp
    # will automatically reverse url to the home page when submitting a form
    def get_absolute_url(self):
        return reverse('posts:home', args=(self.pk,))

    # will order the chirps from newest to oldest
    class Meta:
        ordering = ['-created']

