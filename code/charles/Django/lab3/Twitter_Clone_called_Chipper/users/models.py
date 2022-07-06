from django.db import models


class Users(models.Model):
    username = models.TextField(unique=True, max_length=25)
    password = models.TextField(max_length=25)
    email = models.EmailField()
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)

    # def __str__(self):
    #     return (self.username, self.email, self.first_name, self.last_name)
# Create your models here.
