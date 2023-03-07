from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='revenues'),
    path('', views.tablesjoin, name='capital_receipts'),
    path('<int:capital_receipt_id>', views.capital_receipt, name='capital_receipt'),
    path('search', views.search, name='search'),
]
