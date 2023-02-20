from django.contrib import admin
from .models import Revenue


class RevenueAdmin(admin.ModelAdmin):
    list_display = ('admin_code_id',
                    'appr_prev', 'actual_prev', 'proposed_curr',)
    list_display_links = ('admin_code_id',)
    list_filter = ('admin_code', )
    list_per_page = (15)
    search_fields = ['admin_code__mda_name']


admin.site.register(Revenue, RevenueAdmin)
