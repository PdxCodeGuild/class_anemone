from django.db import models

class GroceryItem(models.Model):
    item_text = models.CharField(max_length=255)

    pub_date = models.DateTimeField(verbose_name='date created')

    def __str__(self):
        return self.item_text
