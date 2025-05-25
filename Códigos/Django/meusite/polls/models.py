from django.db import models

import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    


from polls.models import Pergunta
# Criar uma pergunta
p = Pergunta(texto="Gosta de pizza?", data="2023-10-10")
p.save()  # Salva no banco
# Listar todas as perguntas
Pergunta.objects.all()  # Retorna: <QuerySet [<Pergunta: Gosta de pizza?>]>