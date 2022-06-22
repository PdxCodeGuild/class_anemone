from django.contrib import admin

# import models that we want to register
from .models import GroceryItem

# register the models in the admin panel
admin.site.register(GroceryItem)
