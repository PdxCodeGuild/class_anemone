from django.db import models

# Create your models here.

class Question(models.Model):
    #charfield is for text
    question_text = models.CharField(max_length=255)
    #datetimefield combines a date and time 
    pub_date = models.DateTimeField(verbose_name='date published')

    #customize string representation for an object in this class

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    #on_delete will determine what should happen to the choices
    # after the question to which they are associated is deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.question.question_text + ' ' + self.choice_text
