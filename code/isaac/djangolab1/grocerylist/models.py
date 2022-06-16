from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    # A text description for grocery item.  Max length = 200 characters
    text_description = models.CharField(max_length=200, verbose_name='item description')
    # Date the grocery item was created.
    date_created = models.DateField(verbose_name='date created')
    # Date the item was picked up, completed date.
    date_complete = models.DateField(verbose_name='date completed', null=True, blank=True)
    # A boolean stating whether the items have been picked up or not. True or False
    shop_complete = models.BooleanField(default=False)

    def __str__(self):
        # Label items with their text description
        return self.text_description