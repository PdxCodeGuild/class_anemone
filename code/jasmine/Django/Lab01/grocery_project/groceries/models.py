from django.db import models

# Create your models here.
class GroceryItem(models.Model):

    description = models.CharField(max_length=255)

    created_date = models.DateTimeField(verbose_name='created date')

    completed_date=models.DateTimeField(verbose_name='completed date')

    def __str__(self):
        return self.description