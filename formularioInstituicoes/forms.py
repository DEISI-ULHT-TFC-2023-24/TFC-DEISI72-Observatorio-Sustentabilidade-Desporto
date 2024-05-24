import calendar
import datetime
import locale

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Form
from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Invisible, ReCaptchaV3

from .models import *


class FormNumerosInteiros(ModelForm):
    class Meta:
        model = RespostaNumerica
        fields = ['numero']
        labels = {'numero': ''}

        numero = forms.NumberInput(attrs={
            'required': False,
            'min': 0,
        })


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


class FormEntidade(ModelForm):
    captcha = ReCaptchaField(label='')

    class Meta:
        model = Entidade
        fields = []
        labels = {}


class FormInstalacoes(ModelForm):
    class Meta:
        model = Instalacao
        fields = ['nome', 'morada', 'distrito', 'concelho', 'freguesia', 'telefone', 'email']
        labels = {'nome': "Nome da Instalacao"}

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email",)