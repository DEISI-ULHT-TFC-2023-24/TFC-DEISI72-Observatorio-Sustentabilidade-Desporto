import os
from pathlib import Path

from django.shortcuts import render
from .models import *
from .forms import *


def formulario_view(request):
    questionario = Questionario.objects.get(nome="Questionário Instalações Desportivas")

    temas = {}

    for tema in questionario.temas.all():

        subtemas = {}

        for subtema in SubTema.objects.filter(tema_id=tema.id):
            formulario = {}

            for pergunta in Pergunta.objects.filter(subtema_id=subtema.id):
                if pergunta.subtema.nome == "Observações":
                    formobs = FormTextoLivreObservacoes(prefix=pergunta.id)
                    formulario[pergunta] = formobs

                elif pergunta.tipo == 'NUMERO_INTEIRO':
                    formint = FormNumerosInteiros(prefix=pergunta.id)
                    formulario[pergunta] = formint

                elif pergunta.tipo == 'TEXTO_LIVRE':
                    formtext = FormTextoLivre(prefix=pergunta.id)
                    formulario[pergunta] = formtext

                elif pergunta.tipo == 'ESCOLHA_MULTIPLA':
                    formescolha = FormEscolhaMultipla(prefix=pergunta.id)
                    formescolha.fields['opcao'].queryset = Opcao.objects.filter(pergunta_id=pergunta.id)
                    formulario[pergunta] = formescolha

                elif pergunta.tipo == 'FICHEIRO':
                    formficheiro = FormFicheiro(prefix=pergunta.id)
                    formulario[pergunta] = formficheiro

            subtemas[subtema] = formulario

        temas[tema] = subtemas

    if request.method == "POST":
        print(request.POST)
        post = request.POST

        for chave, resposta_recebida in post.items():
            pergunta_tiporesposta = chave.split('-')
            id_pergunta_retirado = pergunta_tiporesposta[0]
            if id_pergunta_retirado.isdigit():
                tiporesposta = pergunta_tiporesposta[1]

                if tiporesposta == "numero":
                    resposta_num = RespostaNumerica(
                        avaliacao=Avaliacao.objects.get(id=2), #só com o login feito é que fica bom
                        pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                        numero=int(resposta_recebida),
                    )
                    resposta_num.save()

                elif tiporesposta == "texto":
                    resposta_txt = RespostaTextual(
                        avaliacao=Avaliacao.objects.get(id=2),#só com o login feito é que fica bom
                        pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                        texto=resposta_recebida,
                    )
                    resposta_txt.save()

                elif tiporesposta == "opcao":
                    resposta_txt = RespostaTextual(
                        avaliacao=Avaliacao.objects.get(id=2),#só com o login feito é que fica bom
                        pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                        texto=Opcao.objects.get(id=int(resposta_recebida)),
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






    context = {
        'temas': temas,
    }

    return render(request, 'index.html', context)
