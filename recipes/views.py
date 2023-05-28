from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('home 2')

def episodio(request):
    return HttpResponse('episodio')

def cadastro(request):
    return HttpResponse('cadastro')