from django.forms import ModelForm
from django import forms
from .models import *


class FormNumerosInteiros(ModelForm):
    class Meta:
        model = RespostaNumerica
        fields = ['numero']
        labels = {'numero': ''}


class FormTextoLivre(ModelForm):
    class Meta:
        model = RespostaTextual
        fields = ['texto']
        labels = {'texto': ''}


class FormTextoLivreObservacoes(ModelForm):
    class Meta:
        model = RespostaTextual
        fields = ['texto']
        labels = {'texto': ''}

        widgets = {
            'texto': forms.Textarea(attrs={'cols': 25, 'rows': 20}),
        }


class FormEscolhaMultiplaUnica(ModelForm):
    opcao = forms.ModelChoiceField(queryset=Opcao.objects.all(), label=False)

    class Meta:
        model = RespostaTextual
        fields = ['opcao']
        labels = {'opcao': ''}

class FormFicheiro(ModelForm):
    class Meta:
        model = Ficheiro
        fields = ['ficheiro']




class FormEscolhaMultiplaVarias(ModelForm):
    opcoes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label=False)

    class Meta:
        model = RespostaTextual
        fields = ['opcoes']



