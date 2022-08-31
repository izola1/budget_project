from django.db import models
# from ranks.models import Rank
# from departments.models import Department
from mdas.models import Mda
# from sectors.models import Sector
# from sal_structures.models import Sal_Structure
from economic_items.models import Economic_Item
from functions.models import Function
from locations.models import Location


class Personnels(models.Model):
    mdas_id = models.ForeignKey(Mda, on_delete=models.CASCADE)
    ipsas_code = models.ForeignKey(
        Economic_Item, on_delete=models.CASCADE)
    func_code = models.ForeignKey(
        Function, on_delete=models.CASCADE)
    loc_code = models.ForeignKey(
        Location, on_delete=models.CASCADE)
    # departments_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    # rank_id = models.ForeignKey(Rank, on_delete=models.DO_NOTHING)
    # sector_id = models.ForeignKey(Sector, on_delete=models.DO_NOTHING)
    # sal_id = models.ForeignKey(Sal_Structure, on_delete=models.DO_NOTHING)
    # appr_num_staff = models.IntegerField()
    # actual_num_staff = models.IntegerField()
    # prop_num_staff = models.IntegerField()

    appr_prev = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    actual_prev = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    proposed_curr = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    proposed_next = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)

    jan_returns = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    feb_returns = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    april_returns = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    may_returns = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    june_returns = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    july_returns = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    aug_returns = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    sept_returns = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    oct_returns = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    nov_returns = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)
    dec_returns = models.DecimalField(
        default=0.00, max_digits=17, decimal_places=2)

    def __str__(self):
        return self.mdas_id, self.departments_id, self.rank_id, self.sector_id, self.appr_num_staff, self.actual_num_staff, self.prop_num_staff
