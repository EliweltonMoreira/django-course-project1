from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Eliwelton Moreira',
    })


def contact(request):
    return render(request, 'delete-me/temp.html')


def about(request):
    return HttpResponse('about')
