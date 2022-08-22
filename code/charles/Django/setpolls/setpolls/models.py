from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    # CharField is for text
    question_text = models.CharField(max_length=200)

    #DateTimeField combines date and time
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #customize the string represnetation for a Question object
    def __str__(self):
        return self.question_text





class Choice(models.Model):
    #on_delete will determine what should happen to the choices
    # after the question to which they are associated is deletedd
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='choices')
    
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #customize the string represnetation for a Choice object
    def __str__(self):
        return self.question.question_text + ' - ' + self.choice_text
