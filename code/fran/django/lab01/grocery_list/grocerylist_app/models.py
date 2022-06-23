from django.db import models

class GroceryItem(models.Model):
    grocery_item_name = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField()

    # customize the string representation for the GroceryItem object
    def __str__(self):
        return self.grocery_item_name
