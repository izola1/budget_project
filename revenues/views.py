from django.shortcuts import render
from .models import Revenuedata
from django.db import connection
from sqlite3 import Cursor
from unittest import result


def index(request):
    return render(request, 'revenues/revenues.html')


def revenue(request):
    return render(request, 'revenues/revenue.html')


def search(request):
    return render(request, 'revenues/search.html')


def tablesjoin(request):
    cursor = connection.cursor()
    cursor.execute("SELECT mdas_mda.admin_code, mdas_mda.mda_name, economic_items_economic_item.ipsas_code, economic_items_economic_item.ipsas_title, funds_fund.fund_code,funds_fund.description, revenues_revenue.appr_prev, revenues_revenue.actual_prev, revenues_revenue.proposed_curr FROM revenues_revenue LEFT JOIN  economic_items_economic_item ON revenues_revenue.ipsas_code_id=economic_items_economic_item.id LEFT JOIN funds_fund ON revenues_revenue.fund_code_id=funds_fund.id LEFT JOIN mdas_mda ON revenues_revenue.admin_code_id=mdas_mda.id ORDER BY revenues_revenue.id ")
    result = cursor.fetchall()
    return render(request, 'revenues/revenues.html', {'Revenuedata': result})
