from django.contrib import admin
from .models import Fund_Group


class Fund_GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_code', 'description')
    list_display_links = ('group_code',)
    # list_filter = ('func_code', )
    list_per_page = (15)
    ordering = ('id',)
    search_fields = ['group_code']


admin.site.register(Fund_Group, Fund_GroupAdmin)
