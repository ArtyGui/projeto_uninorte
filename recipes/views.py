from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def episodio(request):
    return HttpResponse('episodio')

def cadastro(request):
    return HttpResponse('cadastro')