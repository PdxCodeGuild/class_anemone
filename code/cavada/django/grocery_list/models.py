from django.db import models

# Create your models here.

class GroceryItem(models.Model):

    desc = models.CharField(max_length=50)
    date_created = models.DateTimeField(verbose_name='date created')
    status = models.BooleanField(verbose_name='status')
    date_fulfilled = models.DateTimeField(verbose_name="date fulfilled", blank=True, null=True)


    def __str__(self):
        return self.desc 


"""
from grocery_list.models import GroceryItem
from django.utils import timezone

GroceryItem.objects.all()
<QuerySet []>
g = GroceryItem(desc="t-bone steak",date_created = timezone.now(),status=False, date_fulfilled = timezone.now())
"""