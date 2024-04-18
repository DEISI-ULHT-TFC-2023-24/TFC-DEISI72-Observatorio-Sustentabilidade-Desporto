import calendar
import datetime
import locale

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


class FormMes(ModelForm):
    month_choices = [
        ('', ''),
        ('Janeiro', 'Janeiro'),
        ('Fevereiro', 'Fevereiro'),
        ('Março', 'Março'),
        ('Abril', 'Abril'),
        ('Maio', 'Maio'),
        ('Junho', 'Junho'),
        ('Julho', 'Julho'),
        ('Agosto', 'Agosto'),
        ('Setembro', 'Setembro'),
        ('Outubro', 'Outubro'),
        ('Novembro', 'Novembro'),
        ('Dezembro', 'Dezembro'),
    ]
    month = forms.ChoiceField(choices=month_choices, label='', required=False)

    class Meta:
        model = RespostaTextual
        fields = ['month']
        labels = {'month': ''}


class FormUtilizador(ModelForm):
    class Meta:
        model = Utilizador
        fields = []
        labels = {}