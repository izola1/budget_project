from django.contrib import admin
from .models import Personnels


class PersonnelsAdmin(admin.ModelAdmin):
    # list_display = ('admin_code',  'ipsas_code_id', 'appr_prev',
    #                 'actual_prev', 'proposed_curr', 'prog_code', 'func_code', 'fund_code', 'loc_code',)
    list_display = ('id', 'mdaName', 'ipsasName',
                    'appr_prev', 'actual_prev', 'proposed_curr',)
    # admin_order_field = ('admin_code_id',)
    list_display_links = ('mdaName',)
    list_filter = ('admin_code', )
    list_per_page = (15)
    ordering = ('id',)
    search_fields = ['admin_code__mda_name']

    def mdaName(self, instance):
        return instance.admin_code.mda_name

    def ipsasName(self, instance):
        return instance.ipsas_code.ipsas_title


admin.site.register(Personnels, PersonnelsAdmin)
