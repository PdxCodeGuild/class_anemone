from django.db import models

class GroceryItem(models.Model):
    grocery_text = models.CharField(max_length=50, verbose_name = 'Grocery item')
    date_created = models.DateTimeField(verbose_name='Date created')
    date_completed = models.DateTimeField(null=True, blank=True, verbose_name='Date completed')
    is_complete = models.BooleanField(default=False, verbose_name = 'Completed')

    def __str__(self):
        return self.grocery_text

# superuser username tjwoo