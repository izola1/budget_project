from django.shortcuts import render
from .models import Personneldata
from django.db import connection
from sqlite3 import Cursor
from unittest import result


def index(request):
    return render(request, 'personnels/personnels.html')


def personnel(request):
    return render(request, 'personnels/personnel.html')


def search(request):
    return render(request, 'personnels/search.html')


def tablesjoin(request):
    cursor = connection.cursor()
    cursor.execute("SELECT mdas_mda.admin_code, mdas_mda.mda_name, economic_items_economic_item.ipsas_code, economic_items_economic_item.ipsas_title, functions_function.func_code, functions_function.description,locations_location.loc_code, locations_location.description, funds_fund.fund_code,funds_fund.description, personnels_personnels.appr_prev, personnels_personnels.actual_prev, personnels_personnels.proposed_curr FROM personnels_personnels LEFT JOIN  economic_items_economic_item ON personnels_personnels.ipsas_code_id=economic_items_economic_item.id LEFT JOIN locations_location ON personnels_personnels.loc_code_id=locations_location.id LEFT JOIN funds_fund ON personnels_personnels.fund_code_id=funds_fund.id LEFT JOIN functions_function ON personnels_personnels.func_code_id=functions_function.id LEFT JOIN mdas_mda ON personnels_personnels.admin_code_id=mdas_mda.id ORDER BY personnels_personnels.id ")
    result = cursor.fetchall()
    return render(request, 'personnels/personnels.html', {'Personneldata': result})
