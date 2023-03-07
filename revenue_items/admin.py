from django.contrib import admin
from .models import Revenue_Item


class Revenue_ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'ipsas_code', 'ipsas_title', )
    list_display_links = ('ipsas_title',)
    list_filter = ('ipsas_title', )
    list_per_page = (15)
    ordering = ('id',)
    search_fields = ['ipsas_title']


admin.site.register(Revenue_Item, Revenue_ItemAdmin)
