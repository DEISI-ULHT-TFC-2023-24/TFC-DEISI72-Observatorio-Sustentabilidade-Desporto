from django.forms import ModelForm
from django import forms
from .models import *


class FormNumerosInteiros(ModelForm):
    class Meta:
        model = RespostaNumerica
        fields = ['numero']
        labels = {'numero': ''}

        numero = forms.Textarea(attrs={'required': False})


class FormTextoLivre(ModelForm):
    class Meta:
        model = RespostaTextual
        fields = ['texto']
        labels = {'texto': ''}

        texto = forms.Textarea(attrs={'required': False})


class FormTextoLivreObservacoes(ModelForm):
    class Meta:
        model = RespostaTextual
        fields = ['texto']
        labels = {'texto': ''}

        widgets = {
            'texto': forms.Textarea(attrs={'cols': 25, 'rows': 20}),
        }

        texto = forms.Textarea(attrs={'required': False})


class FormEscolhaMultiplaUnica(ModelForm):
    opcao = forms.ModelChoiceField(queryset=Opcao.objects.all(), label=False, required=False)

    class Meta:
        model = RespostaTextual
        fields = ['opcao']
        labels = {'opcao': ''}

        opcao = forms.Textarea(attrs={'required': False})


class FormEscolhaMultiplaVarias(ModelForm):
    opcoes = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label=False, required=False)

    class Meta:
        model = RespostaTextual
        fields = ['opcoes']


class FormFicheiro(ModelForm):
    class Meta:
        model = Ficheiro
        fields = ['ficheiro']
        labels = {'ficheiro': ''}

        ficheiro = forms.Textarea(attrs={'required': False})
