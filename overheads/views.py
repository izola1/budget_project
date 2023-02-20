from django.shortcuts import render
from .models import Overheaddata
from django.db import connection
from sqlite3 import Cursor
from unittest import result


def index(request):
    return render(request, 'overheads/overheads.html')


def overhead(request):
    return render(request, 'overheads/overhead.html')


def search(request):
    return render(request, 'overheads/search.html')


def tablesjoin(request):
    cursor = connection.cursor()
    cursor.execute("SELECT mdas_mda.admin_code, mdas_mda.mda_name, programmes_programme.code, programmes_programme.description, economic_items_economic_item.ipsas_code, economic_items_economic_item.ipsas_title, functions_function.func_code, functions_function.description,locations_location.loc_code, locations_location.description, funds_fund.fund_code,funds_fund.description, overheads_overhead.appr_prev, overheads_overhead.actual_prev, overheads_overhead.proposed_curr FROM overheads_overhead LEFT JOIN  economic_items_economic_item ON overheads_overhead.ipsas_code_id=economic_items_economic_item.id LEFT JOIN programmes_programme ON overheads_overhead.prog_code_id=programmes_programme.id LEFT JOIN locations_location ON overheads_overhead.loc_code_id=locations_location.id LEFT JOIN funds_fund ON overheads_overhead.fund_code_id=funds_fund.id LEFT JOIN functions_function ON overheads_overhead.func_code_id=functions_function.id LEFT JOIN mdas_mda ON overheads_overhead.admin_code_id=mdas_mda.id ORDER BY overheads_overhead.id ")
    result = cursor.fetchall()
    return render(request, 'overheads/overheads.html', {'Overheaddata': result})
