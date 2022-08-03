import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    # CharField is for text
    question_text = models.CharField(max_length=200)
    # DateTimeField combines a date and a time
    pub_date = models.DateTimeField('date published')
    # customize the string representation for a Question object

    def was_published_recently(self):
        # Checking the publication date if later than current date, minus the day
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # custom string representation for a Question object
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # on_delete will detemine what should happen to the choices
    # after the question to which they are associted with
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # customize the string representation for a Choice object
    def __str__(self):
        return self.question.question_text + ' - ' + self.choice_text