from django.core.validators import RegexValidator
from django.db import models


# TENHO QUE VER, NO FINAL DA MODELAÇÃO, QUAIS ATRIBUTOS VALEM A PENA TER NULL=TRUE

class Tema(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class SubTema(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='subtemas')
    nome = models.CharField(max_length=100)
    resposta_duplicavel = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.nome}"


class Pergunta(models.Model):
    subtema = models.ForeignKey(SubTema, on_delete=models.CASCADE, related_name='perguntas')
    texto = models.TextField(max_length=1000)

    TIPO_RESPOSTA = (
        ('NUMERO_INTEIRO', 'Número Inteiro'),
        ('TEXTO_LIVRE', 'Texto Livre'),
        ('ESCOLHA_MULTIPLA', 'Escolha Múltipla'),
        ('FICHEIRO', 'Ficheiro'),
    )

    tipo = models.CharField(max_length=20, choices=TIPO_RESPOSTA)
    obrigatoria = models.BooleanField()
    def __str__(self):
        return f"{self.texto}"


class Questionario(models.Model):
    temas = models.ManyToManyField(Tema, related_name='questionarios', blank=True)
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

    TIPO_INSTALACAO = (
        ('ARAD', 'Associação de Representantes de Agentes Desportivos'),
        ('APD', 'Associação promotora de desporto'),
        ('ABTE', 'Associação base territorial ou equivalente'),
        ('CLUBE', 'Clube'),
        ('CLUBE_P', 'Clube de praticantes'),
        ('OEIAD', 'Outra entidade com intervenção na área do desporto'),
    )

    tipo_instalacao = models.CharField(max_length=100, choices=TIPO_INSTALACAO)
    rua = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=9, validators=[
        RegexValidator(r'^\d{4}-\d{3}$', message='O código postal deve estar no formato XXXX-XXX')])
    distrito = models.CharField(max_length=100)
    concelho = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    coordenada_x = models.IntegerField(null=True, blank=True)
    coordenada_y = models.IntegerField(null=True, blank=True)
    freguesia = models.CharField(max_length=100)
    nif = models.IntegerField()
    telefone = models.IntegerField()
    email = models.EmailField()
    website = models.CharField(max_length=100, null=True, blank=True)

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
    nome = models.CharField(max_length=100)
    valor = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome


class RespostaTextual(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostasTextuais')
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='respostasTextuais')
    texto = models.CharField(max_length=100)

    def __str__(self):
        return self.texto


class RespostaNumerica(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostasNumericas')
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='respostasNumericas')
    numero = models.IntegerField()

    def __str__(self):
        return f"{self.numero}"

class Ficheiro(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='ficheiros')
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='ficheiros')
    ficheiro = models.FileField(upload_to='media/')

    def __str__(self):
        return f"{self.ficheiro.name}"
