from datetime import timezone
from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse


class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateField()
    completed_date = models.DateField()
    completed  = models.BooleanField()

    def __str__(self):
        return self.text_description

