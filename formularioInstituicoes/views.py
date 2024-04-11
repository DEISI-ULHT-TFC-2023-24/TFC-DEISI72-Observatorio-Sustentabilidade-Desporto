import os
from pathlib import Path

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
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
                if pergunta.subtema.nome == "Observações":
                    formobs = FormTextoLivreObservacoes(prefix=pergunta.id)
                    formulario[pergunta] = formobs

                elif pergunta.tipo == 'NUMERO_INTEIRO':
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

                    escolhas = {}

                    count = 1

                    opcoes = pergunta.opcoes.all().order_by('nome')

                    # Verifica se 'outro' está presente nas opções
                    if opcoes.filter(nome='Outro').exists():
                        # Exclui 'outro' da lista de opções ordenadas
                        opcoes = opcoes.exclude(nome='Outro')
                        # Adiciona 'outro' ao final da lista de opções
                        opcao_outro = pergunta.opcoes.get(nome='Outro')
                        opcoes = list(opcoes) + [opcao_outro]

                    for opcao in opcoes:
                        escolhas[count] = opcao.nome
                        count += 1

                    formescolha.fields['opcoes'].choices = escolhas
                    formulario[pergunta] = formescolha

                elif pergunta.tipo == 'FICHEIRO':
                    formficheiro = FormFicheiro(prefix=pergunta.id)
                    formulario[pergunta] = formficheiro

            subtemas[subtema] = formulario

        temas[tema] = subtemas


def formulario_view(request):
    guarda_perguntas()

    if request.method == "POST":
        print(request.POST)

        post = request.POST
        post_dicionario = dict(post)
        print(post_dicionario['118-opcoes'])

        for chave, resposta_recebida in post_dicionario.items():
            for valor in resposta_recebida:
                if chave == 'tema_subtema':
                    tema_id, subtema_id = valor.split('-')

                    subtema_adicionar = SubTema.objects.get(id=subtema_id)

                    perguntas = {}

                    for pergunta in Pergunta.objects.filter(subtema_id=subtema_id):
                        if pergunta.subtema.nome == "Observações":
                            formobs = FormTextoLivreObservacoes(prefix=pergunta.id)
                            perguntas[pergunta] = formobs

                        elif pergunta.tipo == 'NUMERO_INTEIRO':
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

                            elif tiporesposta == "texto":
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

                                print(Pergunta.objects.get(id=int(id_pergunta_retirado)).opcoes.order_by('nome')[
                                          int(valor)])
                                print(valor)

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

    context = {
        'temas': temas,
    }

    return render(request, 'index.html', context)
