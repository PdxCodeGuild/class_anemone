from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=255)

    #dateTimeField combines a date and a time
    pub_date = models.DateTimeField(verbose_name='date published')

    def _str_(self):
        return self.question_text

class Choice(models.Model):

    #on_delete will determine what should happen to the choices
    # after the question to which they are associated is deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def _str_(self):
        return self.question.question_text + ' - ' + self.choice_text