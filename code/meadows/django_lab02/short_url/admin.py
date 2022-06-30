from django.contrib import admin

#import models that we want to register
from .models import ShortUrl

#register models in admin panel
admin.site.register(ShortUrl)
