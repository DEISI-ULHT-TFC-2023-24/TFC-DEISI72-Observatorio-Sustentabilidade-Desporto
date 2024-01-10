from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.
def index_view(request):
    return render(request, 'index.html', {
        'Tipo_Informacao_Principal': Tipo_Informacao_Principal.objects.all(),
        'Tipo_Informacao_Especifica': Tipo_Informacao_Especifica.objects.all(),
        'Idade_Instalacao_Desportiva': Idade_Instalacao_Desportiva.objects.all(),
        'Balneario': Balneario.objects.all(),
        'Sala_Massagem': Sala_Massagem.objects.all(),
        'Sala_Preparacao': Sala_Preparacao.objects.all(),
        'Sala_Aquecimento': Sala_Aquecimento.objects.all(),
        'Arrecadacao_Material_Desportivo': Arrecadacao_Material_Desportivo.objects.all(),
        'Tribuna_Cabina_Comunicacao_Social': Tribuna_Cabina_Comunicacao_Social.objects.all(),
        'Piscinas': Piscinas.objects.all(),
        'Bancadas': Bancadas.objects.all(),
        'Tipos_Meios_Hidricos_Usados': Tipos_Meios_Hidricos_Usados.objects.all(),
        'Informacoes_Adicionais': Informacoes_Adicionais.objects.all(),
        'Transportes_Publicos': Transportes_Publicos.objects.all(),
        'Parques_Estacionamento': Parques_Estacionamento.objects.all(),
        'Parques_Estacionamento_Bicicletas_Motociclos': Parques_Estacionamento_Bicicletas_Motociclos.objects.all(),
        'Outros_Parques_estacionamento': Outros_Parques_estacionamento.objects.all(),
        'Instalacao_Menos_400_M': Instalacao_Menos_400_M.objects.all(),
        'Instalacao_Inserida_Em': Instalacao_Inserida_Em.objects.all(),
        'Turismo': Turismo.objects.all(),
        'Acessibilidade_Universal': Acessibilidade_Universal.objects.all(),
        'Principais_Tipos_Consumos_Custos_Fontes_Energeticas_Nao_Renovaveis': Principais_Tipos_Consumos_Custos_Fontes_Energeticas_Nao_Renovaveis.objects.all(),
        'Principais_Tipos_Consumos_Custos_Fontes_Energeticas_Renovaveis': Principais_Tipos_Consumos_Custos_Fontes_Energeticas_Renovaveis.objects.all(),
        'Consumos_Energeticos_Anuais': Consumos_Energeticos_Anuais.objects.all(),
        'Custos_Energeticos_Anuais': Custos_Energeticos_Anuais.objects.all(),
        'Media_Numeros_Utilizadores_Anuais': Media_Numeros_Utilizadores_Anuais.objects.all(),
        'Iluminacao': Iluminacao.objects.all(),
        'Climatizacao_Ventilacao': Climatizacao_Ventilacao.objects.all(),
        'Observacoes': Observacoes.objects.all(),
        'Custo_Total_Agua_Anual': Custo_Total_Agua_Anual.objects.all(),
        'Principais_Consumos_Fontes_Abastecimento_Agua': Principais_Consumos_Fontes_Abastecimento_Agua.objects.all(),
        'Descricao_Area_Ambiental': Descricao_Area_Ambiental.objects.all(),
        'Tipo_Producao_Residuos': Tipo_Producao_Residuos.objects.all(),
        'CO2_Equivalente': CO2_Equivalente.objects.all(),
        'Carbono_Associado': Carbono_Associado.objects.all(),
        'Tarifa_Media': Tarifa_Media.objects.all(),
        'Tipo_Meio_Transporte': Tipo_Meio_Transporte.objects.all(),
        'Tipo_Indicadores_Sustentabilidade': Tipo_Indicadores_Sustentabilidade.objects.all(),
        'Modalidade_Atividades': Modalidade_Atividades.objects.all(),
    })


def form_models(request):
    if request.method == "GET":
        Idade_Instalacao_Desportiva = Idade_Instalacao_Desportiva_Form()

        context = {
            'Idade_Instalacao_Desportiva': Idade_Instalacao_Desportiva
        }

        return render(request, 'index.html', context=context)

    else:
        Idade_Instalacao_Desportiva = Idade_Instalacao_Desportiva_Form(request.POST)
        if Idade_Instalacao_Desportiva.is_valid():
            Idade_Instalacao_Desportiva.save()
            Idade_Instalacao_Desportiva = Idade_Instalacao_Desportiva_Form()
            context = {
                'Idade_Instalacao_Desportiva': Idade_Instalacao_Desportiva
            }
            return render(request, 'index.html', context=context)