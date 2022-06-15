from django.contrib import admin

#import models
from .models import Question, Choice

#register models in the admin panel
admin.site.register({Question, Choice})
