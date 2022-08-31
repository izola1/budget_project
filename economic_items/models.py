from django.db import models
from economic_groups.models import Economic_Group


class Economic_Item(models.Model):
    eco_code = models.ForeignKey(Economic_Group, on_delete=models.CASCADE)
    ipsas_code = models.CharField(max_length=8, unique=True)
    ipsas_title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.ipsas_code} {self.ipsas_title}'
