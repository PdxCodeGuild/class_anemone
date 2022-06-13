from django.contrib import admin

from .models import List, Choice

admin.site.register([List, Choice])
