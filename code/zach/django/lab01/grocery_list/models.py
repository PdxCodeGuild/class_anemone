from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    description = models.CharField(max_length=100)
    created_data = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField()
    
    def __str__(self) -> str:
        return self.description