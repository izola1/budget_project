from django.contrib import admin
from .models import Sector


class SectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'sector_code', 'name',)
    list_display_links = ('id', 'sector_code', 'name')
    list_filter = ('sector_code', 'name', )
    list_per_page = (25)


admin.site.register(Sector, SectorAdmin)
