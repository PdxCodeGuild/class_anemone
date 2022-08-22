from django.db import models
from django.urls import reverse

class Chirp(models.Model):
    title = models.CharField(max_length=200)
    chirpname = models.ForeignKey('auth.User', related_name="chirp", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('chirp:detail', args=(self.pk,))

    class Meta:
        ordering = ['-created']