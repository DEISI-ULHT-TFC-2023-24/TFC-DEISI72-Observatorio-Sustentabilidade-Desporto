from django.forms import ModelForm
from django import forms
from .models import *


class FormNumerosInteiros(ModelForm):
    class Meta:
        model = RespostaNumerica
        fields = ['numero']
        labels = {'numero': 'Introduza número'}


class FormTextoLivre(ModelForm):
    class Meta:
        model = RespostaTextual
        fields = ['texto']
        labels = {'texto': 'Introduza o texto'}


class FormEscolhaMultipla(ModelForm):
    opcao = forms.ModelChoiceField(queryset=Opcao.objects.all(), empty_label="Escolha uma opção")

    class Meta:
        model = RespostaTextual
        fields = ['opcao']

    def save(self, commit=True):
        instance = super().save(commit=False)
        opcao_escolhida = self.cleaned_data['opcao']
        instance.texto = opcao_escolhida.nome
        if commit:
            instance.save()
        return instance
