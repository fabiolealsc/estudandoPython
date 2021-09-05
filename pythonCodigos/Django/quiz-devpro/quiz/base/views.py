from django.shortcuts import render

# Create your views here.
from quiz.base.models import Pergunta


def home(req):
    return render(req, 'base/home.html')


def perguntas(req, indice):
    pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]
    contexto = {'indice_da_questao': indice, 'pergunta': pergunta}
    return render(req, 'base/game.html', context=contexto)


def classificacao(req):
    return render(req, 'base/classificacao.html')
