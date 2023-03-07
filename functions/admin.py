from django.contrib import admin
from .models import Function


class FunctionAdmin(admin.ModelAdmin):
    # list_display = ('admin_code',  'ipsas_code_id', 'appr_prev',
    #                 'actual_prev', 'proposed_curr', 'prog_code', 'func_code', 'fund_code', 'loc_code',)
    list_display = ('id', 'func_code', 'description')
    list_display_links = ('func_code',)
    # list_filter = ('func_code', )
    list_per_page = (15)
    ordering = ('id',)
    search_fields = ['func_code']


admin.site.register(Function, FunctionAdmin)
