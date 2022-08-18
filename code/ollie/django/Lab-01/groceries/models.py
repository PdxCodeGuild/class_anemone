from django.db import models

class GroceryItem(models.Model):
    item_text = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.item_text