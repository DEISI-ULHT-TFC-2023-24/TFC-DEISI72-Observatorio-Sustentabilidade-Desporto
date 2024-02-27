from django.shortcuts import render
from .models import *
from .forms import *


def formulario_view(request):
    return render(request, 'index.html', {
        'Temas': Tema.objects.all(),
        'SubTemas': SubTema.objects.all(),
        'Perguntas': Pergunta.objects.all(),
        'Questionarios': Questionario.objects.all(),
        'Entidades': Entidade.objects.all(),
        'Instalacoes': Instalacao.objects.all(),
        'Avaliacoes': Avaliacao.objects.all(),
        'RespostasNumericas': RespostaNumerica.objects.all(),
        'RespostasTextuais': RespostaTextual.objects.all(),
        'Opcoes': Opcao.objects.all()
    })
