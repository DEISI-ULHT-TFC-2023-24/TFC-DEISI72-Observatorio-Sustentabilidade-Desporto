from django.forms import ModelForm
from django import forms
from .models import *


class FormNumerosInteiros(ModelForm):
    class Meta:
        model = RespostaNumerica
        fields = [ 'pergunta', 'avaliacao', 'numero']
        labels = {'numero': 'Introduza número'}


class FormTextoLivre(ModelForm):

    class Meta:
        model = RespostaTextual
        fields = ['pergunta', 'avaliacao', 'texto']
        labels = {'texto': 'Introduza o texto'}


class FormEscolhaMultipla(ModelForm):

    opcao = forms.ModelChoiceField(queryset=Opcao.objects.all(), empty_label="Escolha uma opção")

    class Meta:
        model = RespostaTextual
        fields = ['pergunta', 'avaliacao', 'opcao']

    def save(self, commit=True):
        instance = super().save(commit=False)
        opcao_escolhida = self.cleaned_data['opcao']
        instance.texto = opcao_escolhida.nome  # Salvar o nome da opção escolhida no campo texto
        if commit:
            instance.save()
        return instance