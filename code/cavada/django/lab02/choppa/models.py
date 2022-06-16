from django.db import models

# Create your models here.

import random
import string

letters = string.ascii_letters
digits = string.digits

all_characters = letters + digits 
# print(all_characters)
# counter = 1
# for character in all_characters:
#     print(f"{counter}. {character}")
#     counter += 1
# n = 94

class Code():
    def code_six(self):
        pass_length = 6
        password = []
        pass_length = float(pass_length)
        while len(password) < pass_length:
            password.append(random.choice(all_characters))
        temp_pass = (''.join(password))   
        # print(temp_pass)
        # request = input("""
        # Press enter to reset your password: """)
        print(f"""
            Your temporary password: {temp_pass}
            """)
        return temp_pass

# temp_pass = (''.join(password))    

# what i did was essentially built a list that was empty at first
# and used a while loop adding a random character to the password 
# until it was 10 characters in length, then I converted that list
# of random characters into a single string that can be read as one
# 10 character string, much like you would get from a temp password
# generator

class UrlChoppa(models.Model):
    url = models.CharField(max_length=255)
    pub_date = models.DateTimeField(verbose_name="date published")
    url_code = models.CharField(max_length=6)
    ip_addy = models.CharField(max_length=50)
    def __str__(self):
        return self.url_code
    