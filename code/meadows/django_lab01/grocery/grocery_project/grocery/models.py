from django.db import models

class List(models.Model):
    grocery_list = models.CharField(max_length=200)

    pub_date = models.DateTimeField(verbose_name='date added')

    def __str__(self):
        return self.grocery_list


class Choice(models.Model):
    # on_delete will determine what should happen to the choices after the question to choices 
    grocery_items = models.ForeignKey(List, on_delete=models.CASCADE, related_name='choices') 

    choice_text = models.CharField(max_length=255)
    got_item = models.IntegerField(default=0)

    def __str__(self):
        return self.grocery_items.grocery_list + ' - ' + self.choice_text

