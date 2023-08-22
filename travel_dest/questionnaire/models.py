from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    questionNumber = models.IntegerField(default=-1)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    optionNumber = models.IntegerField(default=-1)

    def __str__(self):
        return self.choice