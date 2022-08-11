from django.contrib import admin
from .models import Mda


class MdaAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_code', 'mda_name', 'sector',)
    list_display_links = ('admin_code', 'mda_name')
    list_filter = ('sector', )
    list_per_page = (25)


admin.site.register(Mda, MdaAdmin)
