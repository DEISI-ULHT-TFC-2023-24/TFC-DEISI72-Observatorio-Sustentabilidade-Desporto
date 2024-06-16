import os

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, FileExtensionValidator
from django.db import models


# TENHO QUE VER, NO FINAL DA MODELAÇÃO, QUAIS ATRIBUTOS VALEM A PENA TER NULL=TRUE

class Tema(models.Model):
    nome = models.CharField(max_length=100)
    ordem_perguntas_formulario = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome


class SubTema(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='subtemas')
    nome = models.CharField(max_length=100)
    resposta_duplicavel = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} - {self.tema.nome}"


class UnidadePergunta(models.Model):
    unidade = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.unidade}"


class Pergunta(models.Model):
    subtema = models.ForeignKey(SubTema, on_delete=models.CASCADE, related_name='perguntas', blank=True, null=True)
    texto = models.TextField(max_length=1000)
    unidade = models.ForeignKey(UnidadePergunta, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='perguntas')

    TIPO_RESPOSTA = (
        ('NUMERO_INTEIRO', 'Número Inteiro'),
        ('TEXTO_LIVRE', 'Texto Livre'),
        ('ESCOLHA_MULTIPLA_UNICA', 'Escolha Múltipla Única'),
        ('ESCOLHA_MULTIPLA_VARIAS', 'Escolha Múltipla Várias'),
        ('FICHEIRO', 'Ficheiro'),
        ('CAMPO_AUTOMATICO', 'Campo Automático'),
        ('MES', 'Mês'),
    )

    tipo = models.CharField(max_length=30, choices=TIPO_RESPOSTA, blank=False, null=True)
    resposta_permite_repetidos = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.texto} : {self.subtema.tema.nome}-{self.subtema.nome}"


class Questionario(models.Model):
    temas = models.ManyToManyField(Tema, related_name='questionarios', blank=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Entidade(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username


class Instalacao(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, related_name='instalacoes')
    nome = models.CharField(max_length=100, blank=True, null=True)

    morada = models.CharField(max_length=100, blank=True, null=True)
    distrito = models.CharField(max_length=100, blank=True, null=True)
    concelho = models.CharField(max_length=100, blank=True, null=True)
    freguesia = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    submetido = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    instalacao = models.ForeignKey(Instalacao, on_delete=models.CASCADE, related_name='avaliacoes')
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE, related_name='avaliacoes')
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.instalacao}: {self.questionario}: {self.ano}"


class Opcao(models.Model):
    pergunta = models.ManyToManyField(Pergunta, related_name='opcoes')
    nome = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}"


class RespostaTextual(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostasTextuais')
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='respostasTextuais')
    texto = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.texto


class RespostaNumerica(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostasNumericas')
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='respostasNumericas')
    numero = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.numero}"



class Ficheiro(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='ficheiros')
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='ficheiros')
    ficheiro = models.FileField(blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def __str__(self):
        return f"{self.ficheiro.name}"
