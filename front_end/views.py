from django.shortcuts import render
from django.views.generic.base import TemplateView
from api.views import ListTransactionsView

class Home(TemplateView):
    template_name = 'index.html'

class Teste(TemplateView):
    template_name = 'list.html'