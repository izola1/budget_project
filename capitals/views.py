from django.shortcuts import render


def index(request):
    return render(request, 'capitals/capitals.html')


def capital(request):
    return render(request, 'capitals/capital.html')


def search(request):
    return render(request, 'capitals/search.html')
