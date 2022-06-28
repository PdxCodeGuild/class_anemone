from datetime import time, timezone
from django.db import models
from django.forms import CharField

class  GroceryItem(models.Model):

    grocery_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date created')
    done = models.BooleanField(db_column='Done', default=False)
    complete_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.grocery_text
