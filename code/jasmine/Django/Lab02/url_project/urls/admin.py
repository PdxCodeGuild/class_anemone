from django.contrib import admin

# Register your models here.

from .models import UrlShortener

admin.site.register(UrlShortener)
