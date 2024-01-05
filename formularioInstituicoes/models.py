from django.db import models


# Create your models here.
class Tipo_Informacao_Principal(models.Model):
    Nome_Tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.Nome_Tipo


class Tipo_Informacao_Especifica(models.Model):
    Nome_Tipo = models.CharField(max_length=100)
    Tipo_Principal = models.ForeignKey(Tipo_Informacao_Principal, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nome_Tipo


class Idade_Instalacao_Desportiva(models.Model):
    Tipo = models.ForeignKey(Tipo_Informacao_Principal, on_delete=models.CASCADE)
    Ano_Construcao = models.IntegerField(max_length=4)
    Ano_Licenciamento = models.IntegerField(max_length=4)
    Ano_Entrada_Funcionamento = models.IntegerField(max_length=4)
    Ano_Ultimas_Obras = models.IntegerField(max_length=4)

    def __str__(self):
        return "Idade da Instalação Desportiva"


class Balneario(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)
    Numero_Unidades_Identicas = models.IntegerField(max_length=5)
    Area = models.IntegerField(max_length=5)
    Numero_Chuveiros = models.IntegerField(max_length=5)
    Numero_Instalacoes_Sanitarias = models.IntegerField(max_length=5)
    Numero_Urinois = models.IntegerField(max_length=5)
    Numero_Lavatorios = models.IntegerField(max_length=5)
    Numero_Cacifos = models.IntegerField(max_length=5)

    def __str__(self):
        return "Balneario"


class Sala_Massagem(models.Model):  # pode ser necessário mudar o tipo de sala de massagem
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)

    AUTONOMA = 'Autonoma'
    INTEGRADA = 'Integrada'

    OPCOES = [
        (AUTONOMA, 'Autonoma'),
        (INTEGRADA, 'Integrada'),
    ]

    Tipo_Sala_Massagem = models.CharField(max_length=10, choices=OPCOES, default='Escolha uma opção')
    Numero_Unidades = models.IntegerField(max_length=5)

    def __str__(self):
        return "Sala de massagem"


class Sala_Preparacao(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)
    Largura = models.IntegerField(max_length=5)
    Altura = models.IntegerField(max_length=5)

    def __str__(self):
        return "Sala de preparação"


class Sala_Aquecimento(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)
    Largura = models.IntegerField(max_length=5)
    Altura = models.IntegerField(max_length=5)

    def __str__(self):
        return "Sala de aquecimento"


class Arrecadacao_Material_Desportivo(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)
    Numero_Unidades = models.IntegerField(max_length=5)
    Area_Total = models.IntegerField(max_length=5)

    def __str__(self):
        return "Arrecadação de material desportivo"


class Tribuna_Cabina_Comunicacao_Social(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)
    Numero_Lugares_Fixos = models.IntegerField(max_length=5)
    Numero_Lugares_Adaptados = models.IntegerField(max_length=5)

    def __str__(self):
        return "Tribuna/Cabina para comunicação social"


class Piscinas(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)
    Comprimento = models.IntegerField(max_length=5)
    Largura = models.IntegerField(max_length=5)
    Altura_Maior = models.IntegerField(max_length=5)
    Altura_Menor = models.IntegerField(max_length=5)
    Volume = models.IntegerField(max_length=5)

    def __str__(self):
        return "Piscinas"


class Bancadas(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)
    Ar_Livre_Num_Espetadores = models.IntegerField(max_length=5)
    Ar_Livre_Num_Espetadores_Mob_Reduzida = models.IntegerField(max_length=5)
    Cobertas_Num_Espetadores = models.IntegerField(max_length=5)
    Cobertas_Num_Espetadores_Mob_Reduzida = models.IntegerField(max_length=5)

    def __str__(self):
        return "Bancadas"


class Tipos_Meios_Hidricos_Usados(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)

    RIO = 'Rio'
    LAGO = 'Lago'
    AGUAS_TRANSICAO = 'Águas de transição'
    AGUAS_COSTEIRAS = 'Águas Costeiras'
    OUTRAS = 'Outras'

    OPCOES = [
        (RIO, 'Rio'),
        (LAGO, 'Lago'),
        (AGUAS_TRANSICAO, 'Águas de transição'),
        (AGUAS_COSTEIRAS, 'Águas Costeiras'),
        (OUTRAS, 'Outras'),
    ]

    Tipo_Meio = models.CharField(max_length=20, choices=OPCOES, default='Escolha uma opção')

    def __str__(self):
        return "Tipos de meios hidricos de superficie usados"


class Informacoes_Adicionais(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)
    Numero_Tanques_Imercao = models.IntegerField(max_length=5)
    Numero_Tanques_Crioterapia = models.IntegerField(max_length=5)
    Numero_Tanques_Terapeuticos = models.IntegerField(max_length=5)
    Numero_Jacuzzis = models.IntegerField(max_length=5)
    Numero_Saunas = models.IntegerField(max_length=5)
    Numero_Salas_Treinos_Tecnicos = models.IntegerField(max_length=5)
    Numero_Postos_Medicos = models.IntegerField(max_length=5)
    Sala_Controlo_Antidoping = models.IntegerField(max_length=5)
    Sala_Reuniao_Entrevista = models.IntegerField(max_length=5)
    Sala_Imprensa = models.IntegerField(max_length=5)

    def __str__(self):
        return "Informações adicionais"


class Transportes_Publicos(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)

    MAIS_400 = 'mais 400m'
    MENOS_400 = 'menos 400m'

    OPCOES = [
        (MAIS_400, 'mais 400m'),
        (MENOS_400, 'menos 400m'),
    ]

    Quantidade = models.CharField(max_length=20, choices=OPCOES, default='Escolha uma opção')

    def __str__(self):
        return "Transportes publicos"


class Parques_Estacionamento(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)
    ATE_50 = 'até 50 lugares'
    ENTRE_51_E_150 = 'entre 51 e 150 lugares'
    ENTRE_151_E_300 = 'entre 151 e 300 lugares'
    ENTRE_301_E_500 = 'entre 301 e 500 lugares'
    ENTRE_501_E_1000 = 'entre 501 e 1000 lugares'
    MAIS_1000 = 'com mais 1000 lugares'

    OPCOES = [
        (ATE_50, 'até 50 lugares'),
        (ENTRE_51_E_150, 'entre 51 e 150 lugares'),
        (ENTRE_151_E_300, 'entre 151 e 300 lugares'),
        (ENTRE_301_E_500, 'entre 301 e 500 lugares'),
        (ENTRE_501_E_1000, 'entre 501 e 1000 lugares'),
        (MAIS_1000, 'com mais 1000 lugares'),
    ]

    Quantidade = models.CharField(max_length=20, choices=OPCOES, default='Escolha uma opção')

    def __str__(self):
        return "Numero de parques de estacionamento"


class Parques_Estacionamento_Bicicletas_Motociclos(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)
    ATE_50 = 'até 50 lugares'
    ENTRE_51_E_150 = 'entre 51 e 150 lugares'
    MAIS_151 = 'com mais 151 lugares'

    OPCOES = [
        (ATE_50, 'até 50 lugares'),
        (ENTRE_51_E_150, 'entre 51 e 150 lugares'),
        (MAIS_151, 'com mais 151 lugares'),
    ]

    Quantidade = models.CharField(max_length=20, choices=OPCOES, default='Escolha uma opção')

    def __str__(self):
        return "Numero de parques de estacionamento para bicicletas e motociclos"


class Outros_Parques_estacionamento(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)
    Numero_Distancia_Menos_400_M = models.IntegerField(max_length=5)

    def __str__(self):
        return "Outros Parques de estacionamento"
