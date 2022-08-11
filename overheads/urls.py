from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='overheads'),
    path('<int:overhead_id>', views.overhead, name='overhead'),
    path('search', views.search, name='search'),
]
