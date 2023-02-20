from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='personnels'),
    path('', views.tablesjoin, name='personnels'),
    path('<int:personnel_id>', views.personnel, name='personnel'),
    path('search', views.search, name='search'),
]
