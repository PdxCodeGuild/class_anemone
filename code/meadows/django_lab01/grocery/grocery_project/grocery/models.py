from django.db import models

class GroceryItem(models.Model):
    store_list = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='Date of purchase')

    def __str__(self):
        return self.store_list

class ItemChoice(models.Model):
    manage_list = models.ForeignKey(GroceryItem, on_delete=models.CASCADE, related_name='choices')
    selected = models.IntegerField(default=0)

    def __str__(self):
        return self.manage_list
