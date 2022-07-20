from xml.dom.pulldom import START_DOCUMENT
from django.contrib import admin

# import models to be registered
from .models import Student

# register the models in the admin panel
admin.site.register(Student)
