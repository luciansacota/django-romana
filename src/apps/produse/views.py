from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

products = [
    {
        'id':1,
        'nume':'paine',
        'cumparat':True,
    },
    
    {
        'id':2,
        'nume':'lapte',
        'cumparat':False,
    },
    
    {
        'id':3,
        'nume':'oua',
        'cumparat':False,
    },
]

def produse(request):
    context = {
        'products':products
    }
    return render(request, 'produse/produse.html', context)