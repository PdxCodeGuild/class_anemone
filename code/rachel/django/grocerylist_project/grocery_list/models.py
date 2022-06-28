from django.db import models

class GroceryItem(models.Model):
    item_text = models.CharField(max_length=255)

    create_date = models.DateTimeField(verbose_name='date created')
    complete_date = models.DateTimeField(verbose_name='date completed', null=True, blank=True)

    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item_text