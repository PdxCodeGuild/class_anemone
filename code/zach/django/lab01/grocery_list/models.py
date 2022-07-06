from curses import def_prog_mode
from django.db import models
from django.utils import timezone
class GroceryItem(models.Model):
    description = models.CharField(max_length=100)
    created_date = models.DateField(default=timezone.now)
    completed_date = models.DateField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.description