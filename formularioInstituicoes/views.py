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
            saveInt.save()

        if formString.is_valid():
            saveString = formString.save(commit=False)
            saveString.save()

        if formEscolha.is_valid():
            saveEscolha = formEscolha.save(commit=False)
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
        'formEscolha': FormEscolhaMultipla(),
    }

    return render(request, 'index.html', context)
