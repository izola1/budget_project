from django.db import models
from sectors.models import Sector
#from subsectors.models import Subsector


class Mda(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.DO_NOTHING)
    #subsector = models.ForeignKey(Subsector, on_delete=models.DO_NOTHING)
    admin_code = models.CharField(max_length=12)
    mda_name = models.CharField(max_length=255)

    def __str__(self):
        return self.mda_name
