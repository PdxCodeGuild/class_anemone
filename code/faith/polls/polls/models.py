from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
pub_date = models.DateTimeField(verbose_name = 'date published')

question_text = models.CharField(max_length=255)

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField(verbose_name='date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return timezone.now()>=self.pub_date >= timezone.now()-datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.question.question_text+'-' + self.choice_text
   