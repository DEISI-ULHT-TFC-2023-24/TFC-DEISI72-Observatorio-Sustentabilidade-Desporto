import os
from pathlib import Path

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.defaulttags import register
from .models import *
from .forms import *

temas = {}


def guarda_perguntas():
    questionario = Questionario.objects.get(nome="Questionário Instalações Desportivas")

    for tema in questionario.temas.all():

        subtemas = {}

        subtemas_todos = SubTema.objects.filter(tema_id=tema.id).order_by('nome')

        if subtemas_todos.filter(nome='Valores relevantes').exists() & subtemas_todos.filter(nome='Outro').exists():
            excluindo_valores = subtemas_todos.exclude(nome='Valores relevantes')
            subtema_valores = subtemas_todos.get(nome='Valores relevantes')

            valores_escluidos = excluindo_valores.exclude(nome='Outro')
            subtema_outro = subtemas_todos.get(nome='Outro')

            subtemas_todos = [subtema_valores] + list(valores_escluidos) + [subtema_outro]

        elif subtemas_todos.filter(nome='Outro').exists():
            valores_escluidos = subtemas_todos.exclude(nome='Outro')
            subtema_outro = subtemas_todos.get(nome='Outro')

            subtemas_todos = list(valores_escluidos) + [subtema_outro]

        elif subtemas_todos.filter(nome='Outros').exists():
            valores_escluidos = subtemas_todos.exclude(nome='Outros')
            subtema_outro = subtemas_todos.get(nome='Outros')

            subtemas_todos = list(valores_escluidos) + [subtema_outro]


        for subtema in subtemas_todos:
            formulario = {}

            perguntas_todos = Pergunta.objects.filter(subtema_id=subtema.id).order_by('texto')

            if perguntas_todos.filter(tipo='ESCOLHA_MULTIPLA_VARIAS').exists():
                valores_escluidos = perguntas_todos.exclude(tipo='ESCOLHA_MULTIPLA_VARIAS')
                pergunta_escluida = perguntas_todos.get(tipo='ESCOLHA_MULTIPLA_VARIAS')

                perguntas_todos = [pergunta_escluida] + list(valores_escluidos)

            elif perguntas_todos.filter(texto='Com potência de').exists():
                valores_escluidos = perguntas_todos.exclude(texto='Com potência de')
                pergunta_escluida = perguntas_todos.get(texto='Com potência de')

                perguntas_todos = list(valores_escluidos) + [pergunta_escluida]

            for pergunta in perguntas_todos:
                if pergunta.tipo == 'NUMERO_INTEIRO':
                    formint = FormNumerosInteiros(prefix=pergunta.id)
                    formulario[pergunta] = formint

                elif pergunta.tipo == 'TEXTO_LIVRE':
                    formtext = FormTextoLivre(prefix=pergunta.id)
                    formulario[pergunta] = formtext

                elif pergunta.tipo == 'ESCOLHA_MULTIPLA_UNICA':
                    formescolha = FormEscolhaMultiplaUnica(prefix=pergunta.id)
                    formescolha.fields['opcao'].queryset = pergunta.opcoes.all().order_by('nome')
                    formulario[pergunta] = formescolha

                elif pergunta.tipo == 'ESCOLHA_MULTIPLA_VARIAS':
                    formescolha = FormEscolhaMultiplaVarias(prefix=pergunta.id)

                    escolhas = []

                    opcoes = pergunta.opcoes.all().order_by('nome')

                    if opcoes.filter(nome='Outro').exists():
                        opcoes = opcoes.exclude(nome='Outro')
                        opcao_outro = pergunta.opcoes.get(nome='Outro')
                        opcoes = list(opcoes) + [opcao_outro]

                    for count, opcao in enumerate(opcoes, start=1):
                        escolha = (str(count), opcao.nome)
                        escolhas.append(escolha)

                    escolhas_final = tuple(escolhas)

                    formescolha.fields['opcoes'].choices = escolhas_final
                    formulario[pergunta] = formescolha

                elif pergunta.tipo == 'FICHEIRO':
                    formficheiro = FormFicheiro(prefix=pergunta.id)
                    formulario[pergunta] = formficheiro

                elif pergunta.tipo == 'MES':
                    formdata = FormMes(prefix=pergunta.id)
                    formulario[pergunta] = formdata

            subtemas[subtema] = formulario

        temas[tema] = subtemas


def post(request):
    if request.method == "POST":
        print(request.POST)

        post = request.POST
        post_dicionario = dict(post)

        for chave, resposta_recebida in post_dicionario.items():
            for valor in resposta_recebida:
                if chave == 'tema_subtema':
                    tema_id, subtema_id = valor.split('-')

                    subtema_adicionar = SubTema.objects.get(id=subtema_id)

                    perguntas = {}

                    for pergunta in Pergunta.objects.filter(subtema_id=subtema_id):
                        if pergunta.tipo == 'NUMERO_INTEIRO':
                            formint = FormNumerosInteiros(prefix=pergunta.id)
                            perguntas[pergunta] = formint

                        elif pergunta.tipo == 'TEXTO_LIVRE':
                            formtext = FormTextoLivre(prefix=pergunta.id)
                            perguntas[pergunta] = formtext

                        elif pergunta.tipo == 'ESCOLHA_MULTIPLA_UNICA':
                            formescolha = FormEscolhaMultiplaUnica(prefix=pergunta.id)
                            formescolha.fields['opcao'].queryset = Opcao.objects.filter(pergunta_id=pergunta.id)
                            perguntas[pergunta] = formescolha

                        elif pergunta.tipo == 'FICHEIRO':
                            formficheiro = FormFicheiro(prefix=pergunta.id)
                            perguntas[pergunta] = formficheiro

                        elif pergunta.tipo == 'MES':
                            formdata = FormMes(prefix=pergunta.id)
                            perguntas[pergunta] = formdata

                    temas.get(Tema.objects.get(id=tema_id))[subtema_adicionar] = perguntas

                    print(temas.get(Tema.objects.get(id=tema_id)).get(SubTema.objects.get(id=subtema_id)).keys())

                else:
                    pergunta_tiporesposta = chave.split('-')
                    id_pergunta_retirado = pergunta_tiporesposta[0]
                    if id_pergunta_retirado.isdigit():
                        tiporesposta = pergunta_tiporesposta[1]

                        if valor != '':
                            if tiporesposta == "numero":
                                resposta_num = RespostaNumerica(
                                    avaliacao=Avaliacao.objects.get(id=3),  # só com o login feito é que fica bom
                                    pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                                    numero=int(valor),
                                )
                                resposta_num.save()

                            elif tiporesposta == "texto" or tiporesposta == "month":
                                resposta_txt = RespostaTextual(
                                    avaliacao=Avaliacao.objects.get(id=3),  # só com o login feito é que fica bom
                                    pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                                    texto=valor,
                                )
                                resposta_txt.save()

                            elif tiporesposta == "opcao":
                                resposta_txt = RespostaTextual(
                                    avaliacao=Avaliacao.objects.get(id=3),  # só com o login feito é que fica bom
                                    pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                                    texto=Opcao.objects.get(id=int(valor)),
                                )
                                resposta_txt.save()


                            elif tiporesposta == "opcoes":

                                resposta_txt = RespostaTextual(
                                    avaliacao=Avaliacao.objects.get(id=3),  # só com o login feito é que fica bom
                                    pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                                    texto=Pergunta.objects.get(id=int(id_pergunta_retirado)).opcoes.order_by('nome')[
                                        int(valor)],
                                )
                                resposta_txt.save()

        print(request.FILES)
        files = request.FILES
        for chave, resposta_recebida in files.items():
            pergunta_tiporesposta = chave.split('-')
            id_pergunta_retirado = pergunta_tiporesposta[0]
            if id_pergunta_retirado.isdigit():
                tipofile = pergunta_tiporesposta[1]

                if tipofile == "ficheiro":
                    print(resposta_recebida)
                    file = Ficheiro(
                        avaliacao=Avaliacao.objects.get(id=2),  # só com o login feito é que fica bom
                        pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                        ficheiro=resposta_recebida
                    )
                    file.save()
        return HttpResponseRedirect(request.path_info)


def formulario_view(request):
    guarda_perguntas()

    post(request)

    context = {
        'temas': temas,
    }

    return render(request, 'index.html', context)


@register.filter(name='split')
def split(value, key):
    return value.split(key)


def dashboard_view(request):
    consumosAnuaisElectricidade = getRespostaNumericaOr0(11)
    consumosAnuaisGasNatural = getRespostaNumericaOr0(21)
    consumosAnuaisPropano = getRespostaNumericaOr0(31)
    consumosAnuaisGasoleo = getRespostaNumericaOr0(41)
    consumosAnuaisGasolina = getRespostaNumericaOr0(51)
    consumosAnuaisFotovoltaica = getRespostaNumericaOr0(61)
    consumosAnuaisBiomassa = getRespostaNumericaOr0(71)
    consumosAnuaisEolica = getRespostaNumericaOr0(81)
    consumosAnuaisTermica = getRespostaNumericaOr0(91)
    consumosAnuaisOutros = getRespostaNumericaOr0(101)

    consumos = [consumosAnuaisElectricidade, consumosAnuaisGasNatural, consumosAnuaisPropano,
                consumosAnuaisGasoleo, consumosAnuaisGasolina, consumosAnuaisFotovoltaica,
                consumosAnuaisBiomassa, consumosAnuaisEolica, consumosAnuaisTermica, consumosAnuaisOutros]

    consumos_labels = ["Electricidade", "Gas Natural", "Propano", "Gasoleo", "Gasolina", "Fotovoltaica", "Biomassa",
                       "Eolica", "Térmica", "Outros"]

    custosAnuaisElectricidade = getRespostaNumericaOr0(12)
    custosAnuaisGasNatural = getRespostaNumericaOr0(22)
    custosAnuaisPropano = getRespostaNumericaOr0(32)
    custosAnuaisGasoleo = getRespostaNumericaOr0(42)
    custosAnuaisGasolina = getRespostaNumericaOr0(52)
    custosAnuaisFotovoltaica = getRespostaNumericaOr0(62)
    custosAnuaisBiomassa = getRespostaNumericaOr0(72)
    custosAnuaisEolica = getRespostaNumericaOr0(82)
    custosAnuaisTermica = getRespostaNumericaOr0(92)
    custosAnuaisOutros = getRespostaNumericaOr0(103)

    custos = [custosAnuaisElectricidade, custosAnuaisGasNatural, custosAnuaisPropano,
              custosAnuaisGasoleo, custosAnuaisGasolina, custosAnuaisFotovoltaica,
              custosAnuaisBiomassa, custosAnuaisEolica, custosAnuaisTermica, custosAnuaisOutros]

    custosconsumo = [
        divByZero(custosAnuaisElectricidade, consumosAnuaisElectricidade),
        divByZero(custosAnuaisGasNatural, consumosAnuaisGasNatural),
        divByZero(custosAnuaisPropano, consumosAnuaisPropano),
        divByZero(custosAnuaisGasoleo, consumosAnuaisGasoleo),
        divByZero(custosAnuaisGasolina, consumosAnuaisGasolina),
        divByZero(custosAnuaisFotovoltaica, consumosAnuaisFotovoltaica),
        divByZero(custosAnuaisBiomassa, consumosAnuaisBiomassa),
        divByZero(custosAnuaisEolica, consumosAnuaisEolica),
        divByZero(custosAnuaisTermica, consumosAnuaisTermica),
        divByZero(custosAnuaisOutros, consumosAnuaisOutros)

    ]

    faturaMinimaElectricidade = getRespostaNumericaOr0(15)
    faturaMinimaGasNatural = getRespostaNumericaOr0(25)
    faturaMinimaPropano = getRespostaNumericaOr0(35)
    faturaMinimaGasoleo = getRespostaNumericaOr0(45)
    faturaMinimaGasolina = getRespostaNumericaOr0(55)
    faturaMinimaFotovoltaica = getRespostaNumericaOr0(65)
    faturaMinimaBiomassa = getRespostaNumericaOr0(75)
    faturaMinimaEolica = getRespostaNumericaOr0(85)
    faturaMinimaTermica = getRespostaNumericaOr0(95)
    faturaMinimaOutros = getRespostaNumericaOr0(106)

    faturasMinimaskWh = [
        getRespostaNumericaOr0(15),
        getRespostaNumericaOr0(25),
        getRespostaNumericaOr0(35),
        getRespostaNumericaOr0(45),
        getRespostaNumericaOr0(55),
        getRespostaNumericaOr0(65),
        getRespostaNumericaOr0(75),
        getRespostaNumericaOr0(85),
        getRespostaNumericaOr0(95),
        getRespostaNumericaOr0(106)
    ]

    faturasMaximaskWh = [
        getRespostaNumericaOr0(18),
        getRespostaNumericaOr0(28),
        getRespostaNumericaOr0(38),
        getRespostaNumericaOr0(48),
        getRespostaNumericaOr0(58),
        getRespostaNumericaOr0(68),
        getRespostaNumericaOr0(78),
        getRespostaNumericaOr0(88),
        getRespostaNumericaOr0(98),
        getRespostaNumericaOr0(103)
    ]

    faturasMinimasEur = [
        getRespostaNumericaOr0(17),
        getRespostaNumericaOr0(27),
        getRespostaNumericaOr0(37),
        getRespostaNumericaOr0(47),
        getRespostaNumericaOr0(57),
        getRespostaNumericaOr0(67),
        getRespostaNumericaOr0(77),
        getRespostaNumericaOr0(87),
        getRespostaNumericaOr0(97),
        getRespostaNumericaOr0(108)
    ]

    faturasMaximasEur = [
        getRespostaNumericaOr0(20),
        getRespostaNumericaOr0(30),
        getRespostaNumericaOr0(40),
        getRespostaNumericaOr0(50),
        getRespostaNumericaOr0(60),
        getRespostaNumericaOr0(70),
        getRespostaNumericaOr0(80),
        getRespostaNumericaOr0(90),
        getRespostaNumericaOr0(100),
        getRespostaNumericaOr0(105)
    ]

    faturas = zip(consumos_labels, faturasMinimaskWh, faturasMinimasEur, faturasMaximaskWh, faturasMaximasEur)

    print(faturas)

    return render(request, 'dashboard.html', {"consumos": consumos, "consumos_labels": consumos_labels,
                                              "custos": custos, "custosconsumo": custosconsumo, "faturas": faturas})


def getRespostaNumericaOr0(pergunta_id):
    if RespostaNumerica.objects.filter(pergunta_id=Pergunta.objects.get(id=pergunta_id)).first():
        return RespostaNumerica.objects.filter(pergunta_id=Pergunta.objects.get(id=pergunta_id)).first().numero
    else:
        return 0


def divByZero(n, d):
    return n / d if d else 0
