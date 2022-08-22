from django.contrib import admin

# Register your models here that we want to register
from .models import Question, Choice

# registger the models in the admin app
admin.site.register([Question,Choice])