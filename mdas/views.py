from django.shortcuts import render
from .models import Mda


def index(request):
    mdas = Mda.objects.all()

    context = {
        'mdas': mdas
    }
    return render(request, 'mdas/mdas.html', context)


def mda(request, mda_id):
    return render(request, 'mdas/mda.html')


def search(request):
    return render(request, 'mdas/search.html')
