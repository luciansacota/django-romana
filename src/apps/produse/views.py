from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def produse(request):
    return HttpResponse('<h2>Lista de cumparaturi</h2>')