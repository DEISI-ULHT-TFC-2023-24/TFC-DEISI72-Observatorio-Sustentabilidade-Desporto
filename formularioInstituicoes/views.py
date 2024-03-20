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

            subtemas[subtema] = formulario

        temas[tema] = subtemas

    if request.method == "POST":
        post = request.POST

        for chave, resposta_recebida in post.items():
            pergunta_tiporesposta = chave.split('-')
            id_pergunta_retirado = pergunta_tiporesposta[0]
            if (id_pergunta_retirado.isdigit()):
                tiporesposta = pergunta_tiporesposta[1]

                if tiporesposta == "numero":
                    resposta_num = RespostaNumerica(
                        avaliacao=Avaliacao.objects.get(id=2), #só com o login feito é que fica bom
                        pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                        numero=int(resposta_recebida)
                    )
                    resposta_num.save()

                elif tiporesposta == "texto":
                    resposta_txt = RespostaTextual(
                        avaliacao=Avaliacao.objects.get(id=2),#só com o login feito é que fica bom
                        pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                        texto=resposta_recebida
                    )
                    resposta_txt.save()

                elif tiporesposta == "opcao":
                    resposta_txt = RespostaTextual(
                        avaliacao=Avaliacao.objects.get(id=2),#só com o login feito é que fica bom
                        pergunta=Pergunta.objects.get(id=int(id_pergunta_retirado)),
                        texto=Opcao.objects.get(id=int(resposta_recebida))
                    )
                    resposta_txt.save()

    context = {
        'temas': temas,
    }

    return render(request, 'index.html', context)


'''
    if request.method == "POST":
                formInt = FormNumerosInteiros(request.POST)
                formString = FormTextoLivre(request.POST)
                formEscolha = FormEscolhaMultipla(request.POST)

                if formInt.is_valid():
                    saveInt = formInt.save(commit=False)

                    pergunta = Pergunta.objects.get(texto="Sala de imprensa")
                    avaliacao = Avaliacao.objects.get(id=2)  # isto vai estar ligado com o login associado ao formulario

                    saveInt.pergunta = pergunta
                    saveInt.avaliacao = avaliacao
                    saveInt.save()

                if formString.is_valid():
                    saveString = formString.save(commit=False)

                    pergunta = Pergunta.objects.get(texto="Sala de imprensa")
                    avaliacao = Avaliacao.objects.get(id=2)  # isto vai estar ligado com o login associado ao formulario

                    saveString.pergunta = pergunta
                    saveString.avaliacao = avaliacao
                    saveString.save()

                if formEscolha.is_valid():
                    saveEscolha = formEscolha.save(commit=False)

                    pergunta = Pergunta.objects.get(texto="Sala de imprensa")
                    avaliacao = Avaliacao.objects.get(id=2)  # isto vai estar ligado com o login associado ao formulario

                    saveEscolha.pergunta = pergunta
                    saveEscolha.avaliacao = avaliacao
                    saveEscolha.save() '''
