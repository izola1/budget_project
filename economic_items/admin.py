from django.contrib import admin
from .models import Economic_Item


# class Economic_itemAdmin(admin.ModelAdmin):
#     list_display = ('id', 'ipsas_code', 'ipsas_title', 'eco_code_id')
#     list_display_links = ('ipsas_code', 'ipsas_title')
#     list_filter = ('eco_code_id', )
#     list_per_page = (25)


admin.site.register(Economic_Item,)
