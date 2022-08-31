from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='mdas'),
    path('', views.tablesjoin, name='mdas'),
    path('<int:mda_id>', views.mda, name='mda'),
    path('search', views.search, name='search'),
]
