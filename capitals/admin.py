from django.contrib import admin
from .models import Capital


class CapitalAdmin(admin.ModelAdmin):
    list_display = ('id',  'appr_prev',
                    'actual_prev', 'proposed_curr',)
    list_display_links = ('appr_prev',)
    list_filter = ('admin_code', )
    list_per_page = (25)


admin.site.register(Capital, CapitalAdmin)
