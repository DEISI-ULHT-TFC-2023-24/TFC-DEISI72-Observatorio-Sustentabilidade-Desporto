from django.db import models

#TENHO QUE VER, NO FINAL DA MODELAÇÃO, QUAIS ATRIBUTOS VALEM A PENA TER NULL=TRUE

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

    TIPO_RESPOSTA = (
        ('NUMERO_INTEIRO', 'Número Inteiro'),
        ('TEXTO_LIVRE', 'Texto Livre'),
        ('ESCOLHA_MULTIPLA', 'Escolha Múltipla'),
    )

    tipo = models.CharField(max_length=20, choices=TIPO_RESPOSTA, null=True)

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


class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='opcoes', default=False)
    opcao = models.CharField(max_length=100)

    def __str__(self):
        return self.opcao


class RespostaNumerica(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostasNumericas', null=True, limit_choices_to={'pergunta__dropdown': True})
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='respostasNumericas')
    texto = models.IntegerField()

    def __str__(self):
        return self.texto


class RespostaTextual(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostasTextuais', null=True)
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='respostasTextuais')
    texto = models.CharField(max_length=100)

    def __str__(self):
        return self.texto
