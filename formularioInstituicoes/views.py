from django.shortcuts import render
from .models import *
from .forms import *


def formulario_view(request):
    if request.method == "POST":
        formInt = FormNumerosInteiros(request.POST)
        formString = FormTextoLivre(request.POST)

        formEscolha = FormEscolhaMultipla(request.POST)

        if formInt.is_valid():
            saveInt = formInt.save(commit=False)

            pergunta_id = request.POST.get('pergunta_id_int')
            pergunta = Pergunta.objects.get(id=pergunta_id)
            avaliacao = Avaliacao.objects.get(id=2)  # isto vai estar ligado com o login associado ao formulario

            saveInt.pergunta = pergunta
            saveInt.avaliacao = avaliacao
            saveInt.save()

        if formString.is_valid():
            saveString = formString.save(commit=False)

            pergunta_id = request.POST.get('pergunta_id_string')

            pergunta = Pergunta.objects.get(id=pergunta_id)
            avaliacao = Avaliacao.objects.get(id=2)  # isto vai estar ligado com o login associado ao formulario

            saveString.pergunta = pergunta
            saveString.avaliacao = avaliacao
            saveString.save()

        if formEscolha.is_valid():
            saveEscolha = formEscolha.save(commit=False)

            pergunta_id = request.POST.get('pergunta_id_escolha')
            pergunta = Pergunta.objects.get(id=pergunta_id)
            avaliacao = Avaliacao.objects.get(id=2)  # isto vai estar ligado com o login associado ao formulario

            saveEscolha.pergunta = pergunta
            saveEscolha.avaliacao = avaliacao
            saveEscolha.save()

    questionario = Questionario.objects.get(nome="Questionário Instalações Desportivas")

    temas = {}

    for tema in questionario.temas.all():

        subtemas = {}

        for subtema in SubTema.objects.filter(tema_id=tema.id):
            formulario = {}

            for pergunta in Pergunta.objects.filter(subtema_id=subtema.id):
                if pergunta.subtema.nome == "Observações":
                    formobs = FormTextoLivreObservacoes()
                    formulario[pergunta] = formobs

                elif pergunta.tipo == 'NUMERO_INTEIRO':
                    formint = FormNumerosInteiros()
                    formulario[pergunta] = formint

                elif pergunta.tipo == 'TEXTO_LIVRE':
                    formtext = FormTextoLivre()
                    formulario[pergunta] = formtext

                elif pergunta.tipo == 'ESCOLHA_MULTIPLA':
                    formescolha = FormEscolhaMultipla()
                    formescolha.fields['opcao'].queryset = Opcao.objects.filter(pergunta_id=pergunta.id)
                    formulario[pergunta] = formescolha



            subtemas[subtema] = formulario

        temas[tema] = subtemas

    context = {
        'temas': temas,
    }

    return render(request, 'index.html', context)
