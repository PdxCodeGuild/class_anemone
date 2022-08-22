from django.contrib import admin

from .models import Post, Comments

admin.site.register([Post, Comments])
