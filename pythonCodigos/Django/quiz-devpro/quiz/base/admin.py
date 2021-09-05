from django.contrib import admin
from quiz.base.models import Pergunta
# Register your models here.


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'enunciado', 'disponivel')
