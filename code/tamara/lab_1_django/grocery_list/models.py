from django.db import models

class GroceryItem(models.Model):
    grocery_text = models.CharField(max_length=50)
    date_created = models.DateTimeField(verbose_name='date created')
    date_completed = models.DateTimeField(verbose_name='date completed')