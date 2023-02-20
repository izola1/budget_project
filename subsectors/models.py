from django.db import models
from sectors.models import Sector


class Subsector(models.Model):
    sector_code = models.ForeignKey(Sector, on_delete=models.DO_NOTHING)
    subsec_code = models.CharField(max_length=12, default="000000000000")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
