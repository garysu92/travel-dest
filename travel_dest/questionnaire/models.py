from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField()

    def __str__(self):
        return self.choice