from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Chirp(models.Model):
    # title of the chirp
    head = models.CharField(max_length=64)
    # body text of the chirp
    body = models.TextField(max_length=300, default="")
    # select the user
    user = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    # date created
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.head

    def get_absolute_url(self):
        return reverse("posts:detail", args=(self.pk,))
    

    # order chirps from newest to oldest
    class Meta:
        ordering = ['-date_created']