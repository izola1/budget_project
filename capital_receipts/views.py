from django.shortcuts import render
from .models import CapitalReceiptdata
from django.db import connection
from sqlite3 import Cursor
from unittest import result


def index(request):
    return render(request, 'capitalreceipts/capitalreceipts.html')


def capital_receipt(request):
    return render(request, 'capitalreceipts/capitalreceipt.html')


def search(request):
    return render(request, 'capitalreceipts/search.html')


def tablesjoin(request):
    cursor = connection.cursor()
    cursor.execute("SELECT mdas_mda.admin_code, mdas_mda.mda_name, economic_items_economic_item.ipsas_code,economic_items_economic_item.ipsas_title, funds_fund.fund_code,funds_fund.description, capital_receipts_capital_receipt.appr_prev,capital_receipts_capital_receipt.actual_prev, capital_receipts_capital_receipt.proposed_curr FROM capital_receipts_capital_receipt LEFT JOIN  economic_items_economic_item ON capital_receipts_capital_receipt.ipsas_code_id=economic_items_economic_item.id LEFT JOIN funds_fund ON capital_receipts_capital_receipt.fund_code_id=funds_fund.id LEFT JOIN mdas_mda ON capital_receipts_capital_receipt.admin_code_id=mdas_mda.id ORDER BY capital_receipts_capital_receipt.id ASC")
    result = cursor.fetchall()
    return render(request, 'capitalreceipts/capitalreceipts.html', {'CapitalReceiptdata': result})
