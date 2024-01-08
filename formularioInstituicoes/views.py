from django.shortcuts import render
from .models import Tipo_Informacao_Principal, Tipo_Informacao_Especifica


# Create your views here.
def index_view(request):
    return render(request, 'index.html', {
        'Tipo_Informacao_Principal': Tipo_Informacao_Principal.objects.all(),
        'Tipo_Informacao_Especifica': Tipo_Informacao_Especifica.objects.all(),
    })
