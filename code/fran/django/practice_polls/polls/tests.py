import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTests(TestCase): # inherits TestCase

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions with a pub_date in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)     # 30 days in the future
        future_question = Question(pub_date=time)   # bc not inserting into db we dont need a ques desc
        self.assertIs(future_question.was_published_recently(), False)  # asserting that thing1=thing2

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

class IndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))  # gets our polls index page
        self.assertEqual(response.status_code, 200) # asserting these two parms are equal
        self.assertContains(response, "No polls are available.")  # note: case sensitive
        self.assertQuerysetEqual(response.context['latest_question_list'], []) # expect an empty list
    
    def test_past_question(self):
        question = create_question(question_text="Past question?", days=-30)  
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])  # should see question created two lines above
    
    def test_future_question(self):
        create_question(question_text="Future question?", days=30) # dont need to tie to a variable bc not expecting question to be returned
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")  # note: case sensitive
        self.assertQuerysetEqual(response.context['latest_question_list'], [])  # shouldnt see anything

    def test_future_question_and_past_question(self):
        question1 = create_question(question_text="Past question?", days=-30)
        question2 = create_question(question_text="Future question?", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question1])

    def test_two_past_questions(self):
        question1 = create_question(question_text="Past question 1?", days=-30)
        question2 = create_question(question_text="Past question 2?", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question2, question1])  # note order

class DetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text="Future question?", days=30)
        response = self.client.get(reverse('polls:detail', args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text="Past question?", days=-30)
        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
        self.assertEquals(response.context['question'], past_question)
        self.assertContains(response, past_question.question_text)
