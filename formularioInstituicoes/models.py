from django.db import models


class Tema(models.Model):
    nome = models.CharField(max_length=100)


class Pergunta(models.Model):
    pergunta = models.CharField(max_length=100)
    tema = models.OneToOneField(Tema, on_delete=models.CASCADE)


class Resposta(models.Model):
    id = models.IntegerField(primary_key=True)
    resposta = models.CharField(max_length=100)
    pergunta = models.OneToOneField(Pergunta, on_delete=models.CASCADE)


class Questionario(models.Model):
    perguntas = models.ForeignKey(Pergunta, on_delete=models.CASCADE)


class Avaliacao(models.Model):
    id = models.IntegerField(primary_key=True)
    ano = models.IntegerField()
    questionario = models.OneToOneField(Questionario, on_delete=models.CASCADE)
    respostas = models.ForeignKey(Resposta, on_delete=models.CASCADE)


class Entidade(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE)
