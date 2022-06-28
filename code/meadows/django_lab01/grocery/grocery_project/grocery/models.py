from django.db import models

class GroceryList(models.Model):
    created_item = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    date_complete = models.DateTimeField(null=True, blank=True)
    created_complete = models.BooleanField()

    def __self__(self):
        return self.created_item
