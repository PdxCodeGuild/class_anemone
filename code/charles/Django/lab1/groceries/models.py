from django.db import models

class Gitem(models.Model):
    item_text = models.CharField(max_length=50)
    item_num = models.IntegerField()
    cdate = models.DateField('date created')
    comdate = models.DateField(null=True, blank=True)
    status = models.BooleanField()

    def __str__(self):
        return self.item_text + ' - ' + str(self.item_num)
