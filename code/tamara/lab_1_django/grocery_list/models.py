from django.db import models

# Pascal case and singular name is customary (inherits models.Model to get all the django stuff)
class GroceryItem(models.Model):
    grocery_text = models.CharField(max_length=50, verbose_name = 'Grocery item')
    date_created = models.DateTimeField(verbose_name='Date created')
    # null=True, blank=True allows the date_completed to be blank
    date_completed = models.DateTimeField(null=True, blank=True, verbose_name='Date completed')
    is_complete = models.BooleanField(default=False, verbose_name = 'Completed')

    # this is so that the grocery_text is printed out instead of 'groceryitem1 etc.)
    def __str__(self):
        return self.grocery_text

# superuser username tjwoo