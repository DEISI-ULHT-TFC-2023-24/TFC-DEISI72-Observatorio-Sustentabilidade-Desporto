from django.db import models


class Tema(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class SubTema(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='subtemas')
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Pergunta(models.Model):
    subtema = models.ForeignKey(SubTema, on_delete=models.CASCADE, related_name='perguntas', null=True)
    texto = models.CharField(max_length=100)

    def __str__(self):
        return self.texto


class Questionario(models.Model):
    temas = models.ManyToManyField(Tema, related_name='questionarios', null=True, blank=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Entidade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Instalacao(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, related_name='instalacoes')
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    instalacao = models.ForeignKey(Instalacao, on_delete=models.CASCADE, related_name='avaliacoes')
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE, related_name='avaliacoes')
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.instalacao}: {self.questionario}"


class Resposta(models.Model):
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='respostas')
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostas')
    texto = models.CharField(max_length=100)

    def __str__(self):
        return self.texto
