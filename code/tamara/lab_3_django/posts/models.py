from django.db import models

class Post(models.Model):
    # thus username (aka 'author') is linked to a foreignkey so they have a unique identifier
    # if the user is deleted then it will CASCADE
            # username = models.ForeignKey('auth.User', related_name="author", on_delete=models.CASCADE)
    username = models.CharField(max_length=20, unique=True)
    # created date will automatically be now
    created = models.DateTimeField(auto_now_add=True)
    # edited date will automatically be now
    edited = models.DateTimeField(auto_now=True)
    # body is the text of the chirp
    body = models.CharField(max_length=128)

    def __str__(self):
        return self.username
        # will show the username of the person who made the chirp in the admin panel
    
    # will order the chirps from newest to oldest
    class Meta:
        ordering = ['-created']
