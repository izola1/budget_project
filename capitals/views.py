from django.shortcuts import render
from .models import Capitaldata
from django.db import connection
from sqlite3 import Cursor
from unittest import result


def index(request):
    return render(request, 'capitals/capitals.html')


def capital(request):
    return render(request, 'capitals/capital.html')


def search(request):
    return render(request, 'capitals/search.html')


def tablesjoin(request):
    cursor = connection.cursor()
    cursor.execute("SELECT mdas_mda.admin_code, mdas_mda.mda_name, programmes_programme.code, programmes_programme.description, economic_items_economic_item.ipsas_code,capitals_capital.proj_Descripton, economic_items_economic_item.ipsas_title, functions_function.func_code, functions_function.description,locations_location.loc_code, locations_location.description, funds_fund.fund_code, funds_fund.description, capitals_capital.appr_prev, capitals_capital.actual_prev, capitals_capital.proposed_curr FROM capitals_capital LEFT JOIN  economic_items_economic_item ON capitals_capital.ipsas_code_id=economic_items_economic_item.id LEFT JOIN programmes_programme ON capitals_capital.prog_code_id=programmes_programme.id LEFT JOIN locations_location ON capitals_capital.loc_code_id=locations_location.id LEFT JOIN funds_fund ON capitals_capital.fund_code_id=funds_fund.id LEFT JOIN functions_function ON capitals_capital.func_code_id=functions_function.id LEFT JOIN mdas_mda ON capitals_capital.admin_code_id=mdas_mda.id ORDER BY capitals_capital.id ")
    result = cursor.fetchall()
    return render(request, 'capitals/capitals.html', {'Capitaldata': result})
