from django.db import models

class Question(models.Model):
    querstion_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.querstion_text

class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choise_text
