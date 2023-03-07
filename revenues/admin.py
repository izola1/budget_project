from django.contrib import admin
from .models import Revenue


class RevenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'mdaName', 'ipsasName',
                    'appr_prev', 'actual_prev', 'proposed_curr',)
    list_display_links = ('mdaName',)
    list_filter = ('admin_code', )
    list_per_page = (25)
    ordering = ('id',)
    search_fields = ['admin_code__mda_name']

    def mdaName(self, instance):
        return instance.admin_code.mda_name

    def ipsasName(self, instance):
        return instance.ipsas_code.ipsas_title


admin.site.register(Revenue, RevenueAdmin)
