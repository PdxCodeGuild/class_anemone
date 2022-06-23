from django.db import models

class Question(models.Model):
    # CharField is for text
    question_text = models.CharField(max_length=255)

    # DateTimeField combines a date and a time
    pub_date = models.DateTimeField(verbose_name='date published')

    # customize the string representation for the Question object
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # on_delete will determine what should happen to the choices
    # after the question to which they are associated is deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255)
    vote = models.IntegerField(default=0)

    # customize the string representation for the Question object
    def __str__(self):
        return self.question.question_text + ' - ' + self.choice_text
