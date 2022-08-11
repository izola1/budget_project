from django.shortcuts import render


def index(request):
    return render(request, 'revenues/revenues.html')


def revenue(request):
    return render(request, 'revenues/revenue.html')


def search(request):
    return render(request, 'revenues/search.html')
