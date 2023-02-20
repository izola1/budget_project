from django.contrib import admin
from .models import Fund


class FundAdmin(admin.ModelAdmin):
    list_display = ('fund_code', 'description')
    list_display_links = ('fund_code',)
    # list_filter = ('func_code', )
    list_per_page = (15)
    search_fields = ['fund_code']


admin.site.register(Fund, FundAdmin)
