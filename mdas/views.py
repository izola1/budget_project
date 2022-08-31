from django.shortcuts import render
from .models import Mda
from .models import Displaydata
from django.db import connection
from sqlite3 import Cursor
from unittest import result


# def index(request):
#     mdas = Mda.objects.all()

#     context = {
#         'mdas': mdas
#     }
#     return render(request, 'mdas/mdas.html', context)


def mda(request, mda_id):
    return render(request, 'mdas/mda.html')


def search(request):
    return render(request, 'mdas/search.html')


def tablesjoin(request):
    cursor = connection.cursor()
    cursor.execute("select mdas_mda.admin_code, mdas_mda.mda_name, sectors_sector.sector_code,  sectors_sector.name from mdas_mda join sectors_sector on sectors_sector.id = mdas_mda.sector_id ")
    result = cursor.fetchall()
    return render(request, 'mdas/mdas.html', {'Displaydata': result})
