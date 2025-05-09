from django.contrib import admin
from .models import Subsector


class SubsectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    list_filter = ('name', )
    list_per_page = (25)
    ordering = ('id',)


admin.site.register(Subsector, SubsectorAdmin)
