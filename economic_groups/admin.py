from django.contrib import admin
from .models import Economic_Group


class Economic_groupAdmin(admin.ModelAdmin):
    list_display = ('id', 'eco_code', 'group_title', 'group_type')
    list_display_links = ('eco_code', 'group_title')
    list_filter = ('group_type', )
    list_per_page = (25)
    ordering = ('id',)
    search_fields = ('group_title',)


admin.site.register(Economic_Group, Economic_groupAdmin)
