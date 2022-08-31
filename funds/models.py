from django.db import models
from fund_groups.models import Fund_Group


class Fund(models.Model):
    group_code = models.ForeignKey(Fund_Group, on_delete=models.CASCADE)
    fund_code = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.fund_code} {self.description}'
