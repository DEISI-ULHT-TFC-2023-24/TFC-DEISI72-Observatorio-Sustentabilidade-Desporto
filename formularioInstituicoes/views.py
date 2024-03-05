from django.shortcuts import render
from .models import *
from .forms import *


def formulario_view(request):
    if request.method == "POST":
        formInt = FormNumerosInteiros(request.POST)
        formString = FormTextoLivre(request.POST)
        pergunta_id_escolha = request.POST.get('pergunta_id_escolha')
        formEscolha = FormEscolhaMultipla(pergunta_id_escolha, request.POST)

        if formInt.is_valid():
            saveInt = formInt.save(commit=False)

            pergunta_id = request.POST.get('pergunta_id_int')

            pergunta = Pergunta.objects.get(id=pergunta_id)
            avaliacao = Avaliacao.objects.get(id=1)  # isto vai estar ligado com o login associado ao formulario

            saveInt.pergunta = pergunta
            saveInt.avaliacao = avaliacao
            saveInt.save()

        if formString.is_valid():
            saveString = formString.save(commit=False)

            pergunta_id = request.POST.get('pergunta_id_string')

            pergunta = Pergunta.objects.get(id=pergunta_id)
            avaliacao = Avaliacao.objects.get(id=1)  # isto vai estar ligado com o login associado ao formulario

            saveString.pergunta = pergunta
            saveString.avaliacao = avaliacao
            saveString.save()

        if formEscolha.is_valid():
            saveEscolha = formEscolha.save(commit=False)

            pergunta_id = request.POST.get('pergunta_id_escolha')

            pergunta = Pergunta.objects.get(id=pergunta_id)
            avaliacao = Avaliacao.objects.get(id=1)  # isto vai estar ligado com o login associado ao formulario

            saveEscolha.pergunta = pergunta
            saveEscolha.avaliacao = avaliacao
            saveEscolha.save()

    context = {
        'Temas': Tema.objects.all(),
        'SubTemas': SubTema.objects.all(),
        'Perguntas': Pergunta.objects.all(),
        'Questionarios': Questionario.objects.all(),
        'Entidades': Entidade.objects.all(),
        'Instalacoes': Instalacao.objects.all(),
        'Avaliacoes': Avaliacao.objects.all(),
        'RespostasNumericas': RespostaNumerica.objects.all(),
        'RespostasTextuais': RespostaTextual.objects.all(),
        'Opcoes': Opcao.objects.all(),
        'formInt': FormNumerosInteiros(),
        'formTexto': FormTextoLivre(),
        'formEscolha': FormEscolhaMultipla(request.POST.get('pergunta_id_escolha')),
    }

    return render(request, 'index.html', context)
