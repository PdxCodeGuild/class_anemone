from django.contrib import admin

# import the class
from .models import GroceryItem

# register the class to the admin panel so that we can use it in the admin panel
# admin panel requires a superuser
    # python manage.py createsuperuser
admin.site.register([GroceryItem])
