from django.contrib import admin

from .models import Rev_Group


class Rev_GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'eco_code', 'group_title', 'group_type', )
    list_display_links = ('group_title',)
    list_filter = ('group_type', )
    list_per_page = (15)
    ordering = ('id',)
    search_fields = ['group_title']


admin.site.register(Rev_Group, Rev_GroupAdmin)
