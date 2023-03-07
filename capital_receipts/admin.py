from django.contrib import admin
from .models import Capital_Receipt


# class Capital_ReceiptAdmin(admin.ModelAdmin):
#     list_display = ('id', 'mda_name', 'appr_prev',
#                     'actual_prev', 'proposed_curr',)
#     # list_display = ('admin_code_id',
#     #                 'appr_prev', 'actual_prev', 'proposed_curr',)
#     list_display_links = ('admin_code',)
#     list_filter = ('admin_code', )
#     list_per_page = (15)
#     search_fields = ['admin_code__mda_name']


class Capital_ReceiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'mdaName', 'ipsasName', 'appr_prev',
                    'actual_prev', 'proposed_curr',)
    list_display_links = ('mdaName',)
    list_filter = ('admin_code', )
    list_per_page = (15)
    ordering = ('id',)
    search_fields = ['admin_code__mda_name']

    def mdaName(self, instance):
        return instance.admin_code.mda_name

    def ipsasName(self, instance):
        return instance.ipsas_code.ipsas_title


admin.site.register(Capital_Receipt, Capital_ReceiptAdmin)
