from django.db import models
from django.forms import BooleanField

# Create your models here.
class GroceryItem(models.Model):
    grocery_description = models.CharField(max_length=255)
    append_time = models.DateTimeField(auto_now_add=True)
    task_completed = models.BooleanField()
    date_completed = models.DateTimeField(verbose_name='date completed', null=True, blank=True)


    


    def __str__(self):
        return self.grocery_description

        



