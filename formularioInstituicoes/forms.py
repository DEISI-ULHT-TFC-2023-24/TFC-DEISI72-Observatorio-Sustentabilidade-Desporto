from django.forms import ModelForm
from django import forms
from .models import *


class Idade_Instalacao_Desportiva_Form(ModelForm):
    class Meta:
        model = Idade_Instalacao_Desportiva
        fields = '__all__'


class Balneario_Form(ModelForm):
    class Meta:
        model = Balneario
        fields = '__all__'

class Sala_Massagem_Form(ModelForm):
    class Meta:
        model = Sala_Massagem
        fields = '__all__'

class Sala_Preparacao_Form(ModelForm):
    class Meta:
        model = Sala_Preparacao
        fields = '__all__'

class Sala_Aquecimento_Form(ModelForm):
    class Meta:
        model = Sala_Aquecimento
        fields = '__all__'

class Arrecadacao_Material_Desportivo_Form(ModelForm):
    class Meta:
        model = Arrecadacao_Material_Desportivo
        fields = '__all__'

class Tribuna_Cabina_Comunicacao_Social_Form(ModelForm):
    class Meta:
        model = Tribuna_Cabina_Comunicacao_Social
        fields = '__all__'

class Piscinas_Form(ModelForm):
    class Meta:
        model = Piscinas
        fields = '__all__'
class Bancadas_Form(ModelForm):
    class Meta:
        model = Bancadas
        fields = '__all__'

class Tipos_Meios_Hidricos_Usados_Form(ModelForm):
    class Meta:
        model = Tipos_Meios_Hidricos_Usados
        fields = '__all__'
class Informacoes_Adicionais_Form(ModelForm):
    class Meta:
        model = Informacoes_Adicionais
        fields = '__all__'
class Transportes_Publicos_Form(ModelForm):
    class Meta:
        model = Transportes_Publicos
        fields = '__all__'
class Parques_Estacionamento_Form(ModelForm):
    class Meta:
        model = Parques_Estacionamento
        fields = '__all__'
class Parques_Estacionamento_Bicicletas_Motociclos_Form(ModelForm):
    class Meta:
        model = Parques_Estacionamento_Bicicletas_Motociclos
        fields = '__all__'
class Outros_Parques_estacionamento_Form(ModelForm):
    class Meta:
        model = Outros_Parques_estacionamento
        fields = '__all__'
class Instalacao_Menos_400_M_Form(ModelForm):
    class Meta:
        model = Instalacao_Menos_400_M
        fields = '__all__'

class Instalacao_Inserida_Em_Form(ModelForm):
    class Meta:
        model = Instalacao_Inserida_Em
        fields = '__all__'
class Turismo_Form(ModelForm):
    class Meta:
        model = Turismo
        fields = '__all__'
class Acessibilidade_Universal_Form(ModelForm):
    class Meta:
        model = Acessibilidade_Universal
        fields = '__all__'
class Principais_Tipos_Consumos_Custos_Fontes_Energeticas_Nao_Renovaveis_Form(ModelForm):
    class Meta:
        model = Principais_Tipos_Consumos_Custos_Fontes_Energeticas_Nao_Renovaveis
        fields = '__all__'
class Principais_Tipos_Consumos_Custos_Fontes_Energeticas_Renovaveis_Form(ModelForm):
    class Meta:
        model = Principais_Tipos_Consumos_Custos_Fontes_Energeticas_Renovaveis
        fields = '__all__'
class Consumos_Energeticos_Anuais_Form(ModelForm):
    class Meta:
        model = Consumos_Energeticos_Anuais
        fields = '__all__'
class Custos_Energeticos_Anuais_Form(ModelForm):
    class Meta:
        model = Custos_Energeticos_Anuais
        fields = '__all__'
class Media_Numeros_Utilizadores_Anuais_Form(ModelForm):
    class Meta:
        model = Media_Numeros_Utilizadores_Anuais
        fields = '__all__'

class Iluminacao_Form(ModelForm):
    class Meta:
        model = Iluminacao
        fields = '__all__'


class Climatizacao_Ventilacao_Form(ModelForm):
    class Meta:
        model = Climatizacao_Ventilacao
        fields = '__all__'


class Observacoes_Form(ModelForm):
    class Meta:
        model = Observacoes
        fields = '__all__'


class Custo_Total_Agua_Anual_Form(ModelForm):
    class Meta:
        model = Custo_Total_Agua_Anual
        fields = '__all__'


class Principais_Consumos_Fontes_Abastecimento_Agua_Form(ModelForm):
    class Meta:
        model = Principais_Consumos_Fontes_Abastecimento_Agua
        fields = '__all__'


class Descricao_Area_Ambiental_Form(ModelForm):
    class Meta:
        model = Descricao_Area_Ambiental
        fields = '__all__'


class Tipo_Producao_Residuos_Form(ModelForm):
    class Meta:
        model = Tipo_Producao_Residuos
        fields = '__all__'


class CO2_Equivalente_Form(ModelForm):
    class Meta:
        model = CO2_Equivalente
        fields = '__all__'


class Carbono_Associado_Form(ModelForm):
    class Meta:
        model = Carbono_Associado
        fields = '__all__'


class Tarifa_Media_Form(ModelForm):
    class Meta:
        model = Tarifa_Media
        fields = '__all__'


class Tipo_Meio_Transporte_Form(ModelForm):
    class Meta:
        model = Tipo_Meio_Transporte
        fields = '__all__'


class Tipo_Indicadores_Sustentabilidade_Form(ModelForm):
    class Meta:
        model = Tipo_Indicadores_Sustentabilidade
        fields = '__all__'


class Modalidade_Atividades_Form(ModelForm):
    class Meta:
        model = Modalidade_Atividades
        fields = '__all__'

