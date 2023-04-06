from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def produse(request):
    context = {
        
    }
    return render(request, 'produse/produse.html', context)