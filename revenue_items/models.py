from django.db import models
from rev_groups.models import Rev_Group


class Revenue_Item(models.Model):
    eco_code = models.ForeignKey(Rev_Group, on_delete=models.CASCADE)
    ipsas_code = models.CharField(max_length=8)
    ipsas_title = models.CharField(max_length=300)
    # type = models.CharField(max_length=8)

    def __str__(self):
        return self.ipsas_title
