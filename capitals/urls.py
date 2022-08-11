from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='capitals'),
    path('<int:capital_id>', views.capital, name='capital'),
    path('search', views.search, name='search'),
]
