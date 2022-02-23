from django.db import models
import random

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=250)
    answer = models.CharField(max_length=60)
    answer_1 = models.CharField(max_length=60)
    answer_2 = models.CharField(max_length=60)
    answer_3 = models.CharField(max_length=60)
    level = models.IntegerField(default=0)
    number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question_text} | Answer: {self.answer} | Level: {self.level} | Number: {self.number}"

    def serialize(self):
        random_answers = [self.answer, self.answer_1, self.answer_2, self.answer_3]
        random.shuffle(random_answers)
        return {
            'question':self.question_text,
            'answers': random_answers,
            'id':self.id
        }