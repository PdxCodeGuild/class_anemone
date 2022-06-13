from django.db import models

class Glist(models.Model):
    glist_text = models.CharField(max_length=50)
    cdate = models.DateField('date created')
    comdate = models.DateField('date to be completed')

    def __str__(self):
        return self.glist_text

class Gitem(models.Model):
    glist = models.ForeignKey(Glist, on_delete = models.CASCADE, related_name='items')
    item_text = models.CharField(max_length=50)
    item_num = models.IntegerField()
    completed = False

    def __str__(self):
        return self.glist.glist_text + ' - ' + self.item_text + ' - ' + str(self.item_num)
