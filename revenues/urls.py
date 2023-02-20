from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='revenues'),
    path('', views.tablesjoin, name='revenues'),
    path('<int:revenue_id>', views.revenue, name='revenue'),
    path('search', views.search, name='search'),
]
