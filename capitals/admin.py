from django.contrib import admin
from .models import Capital


class CapitalAdmin(admin.ModelAdmin):
    # list_display = ('admin_code',  'ipsas_code_id', 'appr_prev',
    #                 'actual_prev', 'proposed_curr', 'prog_code', 'func_code', 'fund_code', 'loc_code',)
    list_display = ('id', 'mdaName', 'proj_Descripton',
                    'appr_prev', 'actual_prev', 'proposed_curr',)
    list_display_links = ('mdaName',)
    list_filter = ('admin_code', )
    list_per_page = (15)
    ordering = ('id',)
    search_fields = ['admin_code__mda_name']

    def mdaName(self, instance):
        return instance.admin_code.mda_name


admin.site.register(Capital, CapitalAdmin)
