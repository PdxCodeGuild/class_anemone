from django.db import models


class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateField()
    completed_date = models.DateField()
    completed  = models.BooleanField()

    def __str__(self):
        return self.text_description
