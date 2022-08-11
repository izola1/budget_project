from django.shortcuts import render


def index(request):
    return render(request, 'personnels/personnels.html')


def personnel(request):
    return render(request, 'personnels/personnel.html')


def search(request):
    return render(request, 'personnels/search.html')
