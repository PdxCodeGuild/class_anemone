from django.db import models

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    uname = models.CharField(max_length=200, default='username_here')
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    age = models.IntegerField()
    
    def __str__(self):
        return self.fname + ' ' + self.lname + ' ' + self.uname