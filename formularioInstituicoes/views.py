import copy
import os
from pathlib import Path

from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.urls import reverse

from .models import *
from .forms import *

perguntas_form = {}


def getEntidade(request) -> Entidade:
    if Entidade.objects.filter(user__id=request.user.id).first():
        return Entidade.objects.filter(user__id=request.user.id).first()
    else:
        return None


def criar_perguntas_form(perguntas_form_object):
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

            elif perguntas_todos.filter(texto='Com valor de').exists():
                valores_escluidos = perguntas_todos.exclude(texto='Com valor de')
                pergunta_escluida = perguntas_todos.get(texto='Com valor de')

                perguntas_todos = list(valores_escluidos) + [pergunta_escluida]

            elif perguntas_todos.filter(texto='Nome').exists():
                valores_escluidos = perguntas_todos.exclude(texto='Nome')
                pergunta_escluida = perguntas_todos.get(texto='Nome')

                perguntas_todos = [pergunta_escluida] + list(valores_escluidos)

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

                    for count, opcao in enumerate(opcoes, start=0):
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

        perguntas_form_object[tema] = subtemas


def post(request, ano_questionario):
    entidade = getEntidade(request)

    instalacao = Instalacao.objects.get(entidade=entidade)

    avaliacoes = Avaliacao.objects.filter(instalacao__nome=instalacao.nome)

    avaliacao = avaliacoes.get(ano=ano_questionario)

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

                    perguntas_form.get(Tema.objects.get(id=tema_id))[subtema_adicionar] = perguntas

                    # print(
                    #     perguntas_form.get(Tema.objects.get(id=tema_id)).get(SubTema.objects.get(id=subtema_id)).keys())

                else:
                    pergunta_tiporesposta = chave.split('-')
                    id_pergunta_retirado = pergunta_tiporesposta[0]
                    if id_pergunta_retirado.isdigit():
                        tiporesposta = pergunta_tiporesposta[1]

                        if valor != '':

                            if tiporesposta == "numero":

                                subtema_repetido = Pergunta.objects.get(
                                    id=id_pergunta_retirado).subtema.resposta_duplicavel
                                pergunta_repetida = Pergunta.objects.get(
                                    id=id_pergunta_retirado).resposta_permite_repetidos

                                if not (subtema_repetido is True and pergunta_repetida is False):
                                    if not (subtema_repetido is False and pergunta_repetida is True):
                                        verificaResposta1 = RespostaNumerica.objects.filter(
                                            avaliacao=avaliacao).filter(
                                            pergunta_id=id_pergunta_retirado)  # só com o login feito é que fica bom
                                        verificaResposta1.delete()  # ver se ele remove apenas o valor da conta associada, e não de todas as contas

                                resposta_num = RespostaNumerica(
                                    avaliacao=avaliacao,  # só com o login feito é que fica bom
                                    pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                                    numero=int(valor),
                                )
                                resposta_num.save()

                            elif tiporesposta == "texto" or tiporesposta == "month":

                                subtema_repetido = Pergunta.objects.get(
                                    id=id_pergunta_retirado).subtema.resposta_duplicavel
                                pergunta_repetida = Pergunta.objects.get(
                                    id=id_pergunta_retirado).resposta_permite_repetidos

                                if not (subtema_repetido is True and pergunta_repetida is False):
                                    if not (subtema_repetido is False and pergunta_repetida is True):
                                        verificaResposta1 = RespostaNumerica.objects.filter(
                                            avaliacao=avaliacao).filter(
                                            pergunta_id=id_pergunta_retirado)  # só com o login feito é que fica bom
                                        verificaResposta1.delete()  # ver se ele remove apenas o valor da conta associada, e não de todas as contas

                                resposta_txt = RespostaTextual(
                                    avaliacao=avaliacao,  # só com o login feito é que fica bom
                                    pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                                    texto=valor,
                                )
                                resposta_txt.save()

                            elif tiporesposta == "opcao":

                                verificaResposta1 = RespostaTextual.objects.filter(
                                    avaliacao=avaliacao).filter(
                                    pergunta_id=id_pergunta_retirado)  # só com o login feito é que fica bom
                                verificaResposta1.delete()  # ver se ele remove apenas o valor da conta associada, e não de todas as contas

                                resposta_txt = RespostaTextual(
                                    avaliacao=avaliacao,  # só com o login feito é que fica bom
                                    pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                                    texto=Opcao.objects.get(id=int(valor)),
                                )
                                resposta_txt.save()


                            elif tiporesposta == "opcoes":

                                resposta_txt = RespostaTextual(
                                    avaliacao=avaliacao,  # só com o login feito é que fica bom
                                    pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                                    texto=Pergunta.objects.get(id=int(id_pergunta_retirado)).opcoes.order_by('nome')[
                                        int(valor)],
                                )
                                resposta_txt.save()

                                pergunta = Pergunta.objects.get(id=id_pergunta_retirado)

                                opcoes_pergunta = RespostaTextual.objects.filter(pergunta_id=pergunta.id)

                                respostas_duplicadas = list()

                                for opcao in opcoes_pergunta:
                                    if (opcao.texto in respostas_duplicadas):
                                        opcao.delete()
                                    else:
                                        respostas_duplicadas.append(opcao.texto)

        # print(request.FILES)
        files = request.FILES
        for chave, resposta_recebida in files.items():
            pergunta_tiporesposta = chave.split('-')
            id_pergunta_retirado = pergunta_tiporesposta[0]
            if id_pergunta_retirado.isdigit():
                tipofile = pergunta_tiporesposta[1]

                if tipofile == "ficheiro":
                    # print(resposta_recebida)
                    file = Ficheiro(
                        avaliacao=avaliacao,  # só com o login feito é que fica bom
                        pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                        ficheiro=resposta_recebida
                    )
                    file.save()


@login_required
def formulario_view(request):
    criar_perguntas_form(perguntas_form)

    post(request, 2024)

    if request.method == "POST" or request.method == "FILES":
        return HttpResponseRedirect(request.path_info)

    context = {
        'perguntas_form': perguntas_form,
    }

    return render(request, 'formulario.html', context)


@login_required
def index_view(request):
    return render(request, 'index.html')


perguntas_respostas_submmit = {}


def guarda_respostas_submmit(entidade, ano_questionario, perguntas_submmit_object):
    instalacao = Instalacao.objects.get(entidade=entidade)

    avaliacoes = Avaliacao.objects.filter(instalacao__nome=instalacao.nome)

    avaliacao = avaliacoes.get(ano=ano_questionario)

    questionario = avaliacao.questionario

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
            respostas = {}

            # if(subtema.resposta_duplicavel is False):

            perguntas_todos = Pergunta.objects.filter(subtema_id=subtema.id).order_by('texto')

            if perguntas_todos.filter(tipo='ESCOLHA_MULTIPLA_VARIAS').exists():
                valores_escluidos = perguntas_todos.exclude(tipo='ESCOLHA_MULTIPLA_VARIAS')
                pergunta_escluida = perguntas_todos.get(tipo='ESCOLHA_MULTIPLA_VARIAS')

                perguntas_todos = [pergunta_escluida] + list(valores_escluidos)

            elif perguntas_todos.filter(texto='Com potência de').exists():
                valores_escluidos = perguntas_todos.exclude(texto='Com potência de')
                pergunta_escluida = perguntas_todos.get(texto='Com potência de')

                perguntas_todos = list(valores_escluidos) + [pergunta_escluida]

            elif perguntas_todos.filter(texto='Com valor de').exists():
                valores_escluidos = perguntas_todos.exclude(texto='Com valor de')
                pergunta_escluida = perguntas_todos.get(texto='Com valor de')

                perguntas_todos = list(valores_escluidos) + [pergunta_escluida]

            elif perguntas_todos.filter(texto='Nome').exists():
                valores_escluidos = perguntas_todos.exclude(texto='Nome')
                pergunta_escluida = perguntas_todos.get(texto='Nome')

                perguntas_todos = [pergunta_escluida] + list(valores_escluidos)

            for pergunta in perguntas_todos:

                if pergunta.tipo == 'NUMERO_INTEIRO':

                    respostas_perguntas = RespostaNumerica.objects.filter(pergunta_id=pergunta.id)
                    respostas_dadas = respostas_perguntas.filter(avaliacao__instalacao_id=instalacao.id)

                    respostas[pergunta] = []
                    for resposta_dada in respostas_dadas:
                        respostas[pergunta].append(resposta_dada)

                elif pergunta.tipo == 'TEXTO_LIVRE' or pergunta.tipo == 'ESCOLHA_MULTIPLA_UNICA' or pergunta.tipo == 'ESCOLHA_MULTIPLA_VARIAS' or pergunta.tipo == 'MES':

                    respostas_perguntas = RespostaTextual.objects.filter(pergunta_id=pergunta.id)
                    respostas_dadas = respostas_perguntas.filter(avaliacao__instalacao_id=instalacao.id).order_by('texto')

                    respostas[pergunta] = []
                    for resposta_dada in respostas_dadas:
                        respostas[pergunta].append(resposta_dada)


                elif pergunta.tipo == 'FICHEIRO':
                    break
                    # print("File")

            subtemas[subtema] = respostas

        perguntas_submmit_object[tema] = subtemas


@login_required
def respostas_view(request):

    entidade = getEntidade(request)
    print(entidade)

    guarda_respostas_submmit(entidade, 2024, perguntas_respostas_submmit)

    context = {
        'perguntas_respostas_submmit': perguntas_respostas_submmit,
    }

    return render(request, 'submmit.html', context)


@login_required
def post_request_submmit(request):
    post = request.POST

    post_dicionario = dict(post)
    lista_items = list(post_dicionario.items())
    print(lista_items)

    if lista_items[0][0] == 'metodo' and lista_items[0][1][0] == 'post':
        if lista_items[1][0] == 'tipo_query' and lista_items[1][1][0] == 'editar':
            print('edit')
        elif lista_items[1][0] == 'tipo_query' and lista_items[1][1][0] == 'remover':
            if lista_items[2][0] == 'tipo_resposta' and lista_items[2][1][0] == 'NUMERO_INTEIRO':
                resposta = RespostaNumerica.objects.get(id=int(lista_items[3][1][0]))
                resposta.delete()

            elif lista_items[2][0] == 'tipo_resposta' and (
                    lista_items[2][1][0] == 'TEXTO_LIVRE' or lista_items[2][1][0] == 'ESCOLHA_MULTIPLA_UNICA'):
                resposta = RespostaTextual.objects.get(id=int(lista_items[3][1][0]))
                resposta.delete()

            elif lista_items[2][0] == 'tipo_resposta' and lista_items[2][1][0] == 'ESCOLHA_MULTIPLA_VARIAS':
                eliminar_valores_escolha_multipla(lista_items)

    return HttpResponse("POST request")


def eliminar_valores_escolha_multipla(lista_items):
    resposta = RespostaTextual.objects.get(id=int(lista_items[3][1][0]))
    subtema_resposta = resposta.pergunta.subtema
    tema = Tema.objects.get(nome=subtema_resposta.tema.nome)
    try:
        subtema = SubTema.objects.filter(tema_id=tema.id).get(nome=resposta.texto)

        perguntas = Pergunta.objects.filter(subtema_id=subtema.id)

        for pergunta in perguntas:
            if pergunta.tipo == 'NUMERO_INTEIRO':
                respostas_eliminar = RespostaNumerica.objects.filter(pergunta_id=pergunta.id)
                for resposta_eliminar in respostas_eliminar:
                    resposta_eliminar.delete()

            elif pergunta.tipo == 'TEXTO_LIVRE' or pergunta.tipo == 'MES' or pergunta.tipo == 'ESCOLHA_MULTIPLA_UNICA':
                respostas_eliminar = RespostaTextual.objects.filter(pergunta_id=pergunta.id)
                for resposta_eliminar in respostas_eliminar:
                    resposta_eliminar.delete()

    except SubTema.DoesNotExist:
        subtema = SubTema.objects.get(id=subtema_resposta.id)
        perguntas = Pergunta.objects.filter(subtema_id=subtema.id)
        lista_perguntas = list(perguntas)

        pergunta_remover = None
        for pergunta in lista_perguntas:
            if pergunta.texto.split("com potência média de")[0].strip() == resposta.texto:
                pergunta_remover = pergunta

        if pergunta_remover != None:
            if pergunta.tipo == 'NUMERO_INTEIRO':
                resposta_eliminar = RespostaNumerica.objects.get(pergunta_id=pergunta.id)
                resposta_eliminar.delete()

            elif pergunta.tipo == 'TEXTO_LIVRE' or pergunta.tipo == 'MES' or pergunta.tipo == 'ESCOLHA_MULTIPLA_UNICA':
                resposta_eliminar = RespostaTextual.objects.get(pergunta_id=pergunta.id)
                resposta_eliminar.delete()
    resposta.delete()


@register.filter(name='split')
def split(value, key):
    return value.split(key)


@login_required
def dashboard_view(request):
    consumosAnuaisElectricidade = getRespostaNumericaOr0(11)
    consumosAnuaisGasNatural = getRespostaNumericaOr0(21)
    consumosAnuaisPropano = getRespostaNumericaOr0(31)
    consumosAnuaisGasoleo = getRespostaNumericaOr0(41)
    consumosAnuaisGasolina = getRespostaNumericaOr0(51)
    consumosAnuaisFotovoltaica = getRespostaNumericaOr0(61)
    consumosAnuaisBiomassa = getRespostaNumericaOr0(208)
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
    custosAnuaisBiomassa = getRespostaNumericaOr0(209)
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

    faturasMinimaskWh = [
        getRespostaNumericaOr0(15),
        getRespostaNumericaOr0(25),
        getRespostaNumericaOr0(35),
        getRespostaNumericaOr0(45),
        getRespostaNumericaOr0(55),
        getRespostaNumericaOr0(65),
        getRespostaNumericaOr0(211),
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
        getRespostaNumericaOr0(214),
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
        getRespostaNumericaOr0(213),
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
        getRespostaNumericaOr0(216),
        getRespostaNumericaOr0(90),
        getRespostaNumericaOr0(100),
        getRespostaNumericaOr0(105)
    ]

    faturas = zip(consumos_labels, faturasMinimaskWh, faturasMinimasEur, faturasMaximaskWh, faturasMaximasEur)

    return render(request, 'dashboard.html', {"consumos": consumos, "consumos_labels": consumos_labels,
                                              "custos": custos, "custosconsumo": custosconsumo, "faturas": faturas})


def getRespostaNumericaOr0(pergunta_id):
    if RespostaNumerica.objects.filter(pergunta_id=Pergunta.objects.get(id=pergunta_id)).first():
        return RespostaNumerica.objects.filter(pergunta_id=Pergunta.objects.get(id=pergunta_id)).first().numero
    else:
        return 0


def divByZero(n, d):
    return n / d if d else 0


def login_view(request):
    print(getEntidade(request))
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect("/index")

    return render(request, 'login.html', {"authForm": AuthenticationForm()})


@login_required
def logout_view(request):
    logout(request)
    return redirect("/login")


def sign_up_view(request):
    formEntidade = FormEntidade(request.POST or None)
    formUser = UserCreationForm(request.POST or None)

    if request.method == "POST":
        user = formUser.save(commit=True)

        utilizador = formEntidade.save(commit=False)

        utilizador.user = user
        utilizador.save()

    return render(request, 'signup.html', {"formUser": formUser, "formUtilizador": formEntidade})
