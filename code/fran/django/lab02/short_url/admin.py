from django.contrib import admin

# import model to be registered
from .models import ShortUrlCode

# register the model in the admin panel
admin.site.register(ShortUrlCode)
