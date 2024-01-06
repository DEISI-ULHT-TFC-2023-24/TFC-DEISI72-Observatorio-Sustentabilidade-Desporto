from django.db import models


# Create your models here.
class Tipo_Informacao_Principal(models.Model):  # Coluna C EXCEL
    Nome_Tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.Nome_Tipo


class Tipo_Informacao_Especifica(models.Model):  # Coluna D EXCEL
    Nome_Tipo = models.CharField(max_length=100)
    Tipo_Principal = models.ForeignKey(Tipo_Informacao_Principal, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nome_Tipo


class Idade_Instalacao_Desportiva(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)
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

    Tipo_Sala_Massagem = models.CharField(max_length=10, choices=OPCOES, default=AUTONOMA)
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

    Tipo_Meio = models.CharField(max_length=20, choices=OPCOES, default=RIO)

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

    Quantidade = models.CharField(max_length=20, choices=OPCOES, default=MAIS_400)

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

    Quantidade = models.CharField(max_length=20, choices=OPCOES, default=ATE_50)

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

    Quantidade = models.CharField(max_length=20, choices=OPCOES, default=ATE_50)

    def __str__(self):
        return "Numero de parques de estacionamento para bicicletas e motociclos"


class Outros_Parques_estacionamento(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)
    Numero_Distancia_Menos_400_M = models.IntegerField(max_length=5)

    def __str__(self):
        return "Outros Parques de estacionamento"


class Instalacao_Menos_400_M(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)

    ENSINO_BASICO = 'Ensino Basico'
    ENSINO_SECUNDARIO = 'Ensino Secundario'
    ENSINO_SUPERIOR = 'Ensino Superior'

    OPCOES = [
        (ENSINO_BASICO, 'Ensino Basico'),
        (ENSINO_SECUNDARIO, 'Ensino Secundario'),
        (ENSINO_SUPERIOR, 'Ensino Superior'),
    ]

    Tipo_Ensino = models.CharField(max_length=20, choices=OPCOES, default=ENSINO_BASICO)

    def __str__(self):
        return "Instalações a menos de 400 m"


class Instalacao_Inserida_Em(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)

    ESTABELECIMENTO_BASICO = 'Estabelecimento Básico'
    ESTABELECIMENTO_ENSINO_SECUNDARIO = 'Estabelecimento de Ensino Secundário'
    ESTABELECIMENTO_ENSINO_SUPERIOR_OU_EQUIPERADO = 'Estabelecimento de Ensino Superior ou Equiparado'

    OPCOES = [
        (ESTABELECIMENTO_BASICO, 'Estabelecimento Básico'),
        (ESTABELECIMENTO_ENSINO_SECUNDARIO, 'Estabelecimento de Ensino Secundário'),
        (ESTABELECIMENTO_ENSINO_SUPERIOR_OU_EQUIPERADO, 'Estabelecimento de Ensino Superior ou Equiparado'),
    ]

    Tipo_Estabelecimento = models.CharField(max_length=20, choices=OPCOES, default=ESTABELECIMENTO_BASICO)

    def __str__(self):
        return "Instalação inserida em"


class Turismo(models.Model):
    Nome_Tipo_Informacao_Especifica = models.OneToOneField(Tipo_Informacao_Especifica, on_delete=models.CASCADE,
                                                           default=1)
    INSTALACAO_MENOS_400_M_ALOJAMENTO = 'Instalação a menos de 400m de alojamento turístico'
    INSTALACAO_INTEGRADA_EMPREENDIMENTO = 'Instalação integrada em empreendimento turístico'

    OPCOES = [
        (INSTALACAO_MENOS_400_M_ALOJAMENTO, 'Instalação a menos de 400m de alojamento turístico'),
        (INSTALACAO_INTEGRADA_EMPREENDIMENTO, 'Instalação integrada em empreendimento turístico'),
    ]

    Tipo_Turismo = models.CharField(max_length=20, choices=OPCOES, default=INSTALACAO_MENOS_400_M_ALOJAMENTO)

    def __str__(self):
        return "Turismo"


class Acessibilidade_Universal(models.Model):
    Tipo_Informacao = models.ForeignKey(Tipo_Informacao_Principal, on_delete=models.CASCADE)

    NAO_ACESSIVEL = 'Não acessível'
    ACESSIVEL_AREA_PUBLICO = 'Acessível área de público'
    ACESSIVEL_AREA_PRATICA_DESPORTIVA = 'Acessível área de prática desportiva'
    ACESSIVEL_BALNEARIOS = 'Acessível balneários'

    OPCOES = [
        (NAO_ACESSIVEL, 'Não acessível'),
        (ACESSIVEL_AREA_PUBLICO, 'Acessível área de público'),
        (ACESSIVEL_AREA_PRATICA_DESPORTIVA, 'Acessível área de prática desportiva'),
        (ACESSIVEL_BALNEARIOS, 'Acessível balneários'),
    ]

    Acessibilidade = models.CharField(max_length=20, choices=OPCOES, default=NAO_ACESSIVEL)
    Nr_Lugares_Estacionamento_Mobilidade_reduzida = models.IntegerField(max_length=2)

    def __str__(self):
        return "Acessibilidade_Universal"


class Principais_Tipos_Consumos_Custos_Fontes_Energeticas_Nao_Renovaveis(models.Model):
    # A Energia térmica proveniente de cogeração/redes urbanas têm duas opções

    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)

    ELETRICIDADE = 'Eletricidade'
    GAS_NATURAL = 'Gás Natural'
    GAS_PROPANO = 'Gás Propano'
    GAS_GARRAFA = 'Gás de garrafa'
    GASOLEO = 'Gasóleo'
    ENERGIA_FOTOVOLTAICA = 'Energia Fotovoltaica'
    BIOMASSA = 'Biomassa'
    ENERGIA_EOLICA = 'Energia Eólica'
    ENERGIA_TERMICA_PROVENIENTE_COGERACAO_REDES_URBANAS = 'Energia térmica proveniente de cogeração/redes urbanas'
    OUTROS = 'Outros'

    OPCOES = [
        (ELETRICIDADE, 'Eletricidade'),
        (GAS_NATURAL, 'Gás Natural'),
        (GAS_PROPANO, 'Gás Propano'),
        (GAS_GARRAFA, 'Gás de garrafa'),
        (GASOLEO, 'Gasóleo'),
        (ENERGIA_FOTOVOLTAICA, 'Energia Fotovoltaica'),
        (BIOMASSA, 'Biomassa'),
        (ENERGIA_EOLICA, 'Energia Eólica'),
        (ENERGIA_TERMICA_PROVENIENTE_COGERACAO_REDES_URBANAS, 'Energia térmica proveniente de cogeração/redes urbanas'),
        (OUTROS, 'Outros'),
    ]

    Tipo_Energia = models.CharField(max_length=20, choices=OPCOES, default=ELETRICIDADE)

    def __str__(self):
        return "Principais consumos e custos das fontes energéticas não renováveis"


class Principais_Tipos_Consumos_Custos_Fontes_Energeticas_Renovaveis(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)

    ENERGIA_FOTOVOLTAICA = 'Energia Fotovoltaica'
    ENERGIA_SISTEMAS_SOLARES_TERMICOS = 'Energia de sistemas solares térmicos'
    BIOMASSA = 'Biomassa'
    ENERGIA_EOLICA = 'Energia Eólica'
    ENERGIA_HIDRAULICA = 'Energia Hidraulica'

    OPCOES = [
        (ENERGIA_FOTOVOLTAICA, 'Energia Fotovoltaica'),
        (ENERGIA_SISTEMAS_SOLARES_TERMICOS, 'Energia de sistemas solares térmicos'),
        (BIOMASSA, 'Biomassa'),
        (ENERGIA_EOLICA, 'Energia Eólica'),
        (ENERGIA_HIDRAULICA, 'Energia Hidraulica'),
    ]

    Tipo_Energia = models.CharField(max_length=20, choices=OPCOES, default=ENERGIA_FOTOVOLTAICA)

    def __str__(self):
        return "Principais tipos consumos e custos das fontes energéticas renováveis"


class Consumos_Energeticos_Anuais(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)
    Valor_Consumo = models.IntegerField(max_length=10)

    def __str__(self):
        return "Consumos energéticos anuais/fonte energética"


class Custos_Energeticos_Anuais(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)
    Valor_Custo = models.IntegerField(max_length=10)

    def __str__(self):
        return "Custos energéticos anuais/fonte energética"


class Media_Numeros_Utilizadores_Anuais(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)
    Media_Utilizadores = models.IntegerField(max_length=10)

    def __str__(self):
        return "Média de número de utilizadores anuais"


class Iluminacao(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)

    ILUMINACAO_INTERIOR_GERAL = 'Iluminação Interior Geral'
    ILUMINACAO_INTERIOR_DESPORTIVA = 'Iluminação Interior Desportiva'
    ILUMINACAO_EXTERIOR_GERAL = 'Iluminação Exterior Geral'
    ILUMINACAO_EXTERIOR_DESPORTIVA = 'Iluminação Exterior Desportiva'

    OPCOES = [
        (ILUMINACAO_INTERIOR_GERAL, 'Iluminação Interior Geral'),
        (ILUMINACAO_INTERIOR_DESPORTIVA, 'Iluminação Interior Desportiva'),
        (ILUMINACAO_EXTERIOR_GERAL, 'Iluminação Exterior Geral'),
        (ILUMINACAO_EXTERIOR_DESPORTIVA, 'Iluminação Exterior Desportiva'),
    ]

    Tipo_Ilumicacao = models.CharField(max_length=20, choices=OPCOES, default=ILUMINACAO_INTERIOR_GERAL)

    def __str__(self):
        return "Iluminação"


class Climatizacao_Ventilacao(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)

    SISTEMA_CALDEIRA = 'Sistema de Caldeira'
    BOMBA_CALOR = 'Bomba de Calor'
    TERMOACUMULADORES = 'Termoacumuladores com resistências Elétricas'
    SISTEMAS_RECUPERACAO_CALOR = 'Sistemas de recuperação de calor'
    SISTEMAS_APOIO_SOLAR_TERMICO = 'Sistema de Apoio Solar Térmico'

    OPCOES = [
        (SISTEMA_CALDEIRA, 'Sistema de Caldeira'),
        (BOMBA_CALOR, 'Bomba de Calor'),
        (TERMOACUMULADORES, 'Termoacumuladores com resistências Elétricas'),
        (SISTEMAS_RECUPERACAO_CALOR, 'Sistemas de recuperação de calor'),
        (SISTEMAS_APOIO_SOLAR_TERMICO, 'Sistema de Apoio Solar Térmico'),
    ]

    Tipo_Climatizacao_Ventilacao = models.CharField(max_length=20, choices=OPCOES, default=SISTEMA_CALDEIRA)

    def __str__(self):
        return "Climatização/Ventilação"


class Observacoes(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)
    Observacoes = models.CharField(max_length=500)

    def __str__(self):
        return "Observações"


class Custo_Total_Agua_Anual(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)
    Custo_Agua_Anual = models.IntegerField(max_length=10)

    def __str__(self):
        return "Custo total de água anual"


class Principais_Consumos_Fontes_Abastecimento_Agua(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)

    ABASTECIMENTO_PUBLICO = 'Abastecimento Público'
    CAPTACOES_PROPRIAS = 'Captações próprias'
    AGUAS_PLUVIAIS = 'Águas pluviais'
    AGUAS_CINZENTAS = 'Águas cinzentas'
    OUTRAS_ORIGENS = 'Outras origens'

    OPCOES = [
        (ABASTECIMENTO_PUBLICO, 'Abastecimento Público'),
        (CAPTACOES_PROPRIAS, 'Captações próprias'),
        (AGUAS_PLUVIAIS, 'Águas pluviais'),
        (AGUAS_CINZENTAS, 'Águas cinzentas'),
        (OUTRAS_ORIGENS, 'Outras origens'),
    ]

    Tipo_Climatizacao_Ventilacao = models.CharField(max_length=20, choices=OPCOES, default=ABASTECIMENTO_PUBLICO)

    def __str__(self):
        return "Principais consumos das fontes de abastecimento de água"


class Descricao_Area_Ambiental(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)
    Tipo_Vegetacao = models.CharField(max_length=500)
    Tipo_Solo = models.CharField(max_length=500)

    def __str__(self):
        return "Descrição da área ambiental"


class Tipo_Producao_Residuos(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)

    ORGANICOS = 'Orgânicos'
    PLASTICOS = 'Plásticos'
    PAPEL = 'Papel'
    VIDROS = 'Vidros'
    ELETRONICOS = 'Eletónicos'
    OUTROS = 'Outros'

    OPCOES = [
        (ORGANICOS, 'Orgânicos'),
        (PLASTICOS, 'Plásticos'),
        (PAPEL, 'Papel'),
        (VIDROS, 'Vidros'),
        (ELETRONICOS, 'Eletónicos'),
        (OUTROS, 'Outros'),
    ]

    Tipo_Climatizacao_Ventilacao = models.CharField(max_length=20, choices=OPCOES, default=ORGANICOS)

    def __str__(self):
        return "Tipos de produção de Resíduos"


class CO2_Equivalente(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)
    CO2 = models.IntegerField(max_length=10)

    def __str__(self):
        return "Co2 equivalente"


class Carbono_Associado(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)
    Carbono = models.IntegerField(max_length=10)

    def __str__(self):
        return "Carbono associado a cada fatura de eletricidade média mensal"


class Tarifa_Media(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)
    Tarifa = models.IntegerField(max_length=10)

    def __str__(self):
        return "Tarifa média (€/kWh)"


class Tipo_Meio_Transporte(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)

    CARRO_PASSAGEIROS = 'Carros de passageiros'
    CARRINHA = 'Carrinha'
    AUTOCARRO = 'Autocarro'
    BARCO = 'Barco'
    OUTRO = 'Outro'

    OPCOES = [
        (CARRO_PASSAGEIROS, 'Carros de passageiros'),
        (CARRINHA, 'Carrinha'),
        (AUTOCARRO, 'Autocarro'),
        (BARCO, 'Barco'),
        (OUTRO, 'Outro'),
    ]

    Tipo_Climatizacao_Ventilacao = models.CharField(max_length=20, choices=OPCOES, default=CARRO_PASSAGEIROS)

    def __str__(self):
        return "Tipo de meio de transporte"


class Tipo_Indicadores_Sustentabilidade(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)

    REDUCAO_RESIDUOS = 'Redução de Resíduos '
    RECUPERACAO_MATERIAIS = ' Recuperação de Materiais'
    ESTRATEGIAS_CONSERVACAO_AGUA = 'Estratégias de Conservação de Água'
    PROGRAMAS_ENVOLVIMENTO_COMUNIDADE_ATIVIDADES_DESPORTIVAS = 'Programas para Envolvimento da Comunidade em Atividades Desportivas'
    OTIMIZACAO_RECURSOS = 'Otimização de Recursos'
    PARCERIAS_EMPRESAS_LOCAIS_SUSTENTAVEIS = 'Parcerias com Empresas Locais Sustentáveis'
    PROJETOS_EFICIENCIA_ENERGETICA_SUSTENTABILIDADE = 'Projetos de Eficiência Energética e Sustentabilidade'
    OUTRO = 'Outro'

    OPCOES = [
        (REDUCAO_RESIDUOS, 'Redução de Resíduos'),
        (RECUPERACAO_MATERIAIS, ' Recuperação de Materiais'),
        (ESTRATEGIAS_CONSERVACAO_AGUA, 'Estratégias de Conservação de Água'),
        (PROGRAMAS_ENVOLVIMENTO_COMUNIDADE_ATIVIDADES_DESPORTIVAS,
         'Programas para Envolvimento da Comunidade em Atividades Desportivas'),
        (OTIMIZACAO_RECURSOS, 'Otimização de Recursos'),
        (PARCERIAS_EMPRESAS_LOCAIS_SUSTENTAVEIS, 'Parcerias com Empresas Locais Sustentáveis'),
        (PROJETOS_EFICIENCIA_ENERGETICA_SUSTENTABILIDADE, 'Projetos de Eficiência Energética e Sustentabilidade'),
        (OUTRO, 'Outro'),
    ]

    Tipo_Indicadores_Sustentabilidade = models.CharField(max_length=20, choices=OPCOES, default=REDUCAO_RESIDUOS)

    def __str__(self):
        return "Indicador de Sustentabilidade da Instalação"


class Modalidade_Atividades(models.Model):
    Tipo_Informacao = models.OneToOneField(Tipo_Informacao_Principal, on_delete=models.CASCADE,
                                           default=1)
    Tipos_Modalidades = models.CharField(max_length=500)

    def __str__(self):
        return "Modalidades/atividades"
