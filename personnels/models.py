from django.db import models
from ranks.models import Rank
from departments.models import Department
from mdas.models import Mda
from sectors.models import Sector
from sal_structures.models import Sal_Structure


class Personnels(models.Model):
    mdas_id = models.ForeignKey(Mda, on_delete=models.CASCADE)
    departments_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    rank_id = models.ForeignKey(Rank, on_delete=models.DO_NOTHING)
    sector_id = models.ForeignKey(Sector, on_delete=models.DO_NOTHING)
    sal_id = models.ForeignKey(Sal_Structure, on_delete=models.DO_NOTHING)
    appr_num_staff = models.IntegerField()
    actual_num_staff = models.IntegerField()
    prop_num_staff = models.IntegerField()

    def __str__(self):
        return self.mdas_id, self.departments_id, self.rank_id, self.sector_id, self.appr_num_staff, self.actual_num_staff, self.prop_num_staff
