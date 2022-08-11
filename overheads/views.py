from django.shortcuts import render


def index(request):
    return render(request, 'overheads/overheads.html')


def overhead(request):
    return render(request, 'overheads/overhead.html')


def search(request):
    return render(request, 'overheads/search.html')
