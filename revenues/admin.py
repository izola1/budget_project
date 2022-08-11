from django.contrib import admin
from .models import Revenue


class RevenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_code', 'mda_name', 'sector', 'subsector')
    list_display_links = ('admin_code', 'mda_name')
    list_filter = ('sector', )
    list_per_page = (25)


admin.site.register(Revenue)
