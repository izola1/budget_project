from django.db import models
from mdas.models import Mda
# from economic_groups.models import Economic_Group
# from rev_groups.models import Rev_Group
# from economic_items.models import Economic_Item
from revenue_items.models import Revenue_Item
from funds.models import Fund


class Revenue(models.Model):
    admin_code = models.ForeignKey(Mda, on_delete=models.CASCADE)
    ipsas_code = models.ForeignKey(Revenue_Item, on_delete=models.CASCADE)
    # ipsas_code_id = models.ForeignKey(Economic_Item, on_delete=models.CASCADE)
    # eco_code = models.ForeignKey(Rev_Group, on_delete=models.CASCADE)
    # eco_code_id = models.ForeignKey(Economic_Group, on_delete=models.CASCADE)
    fund_code = models.ForeignKey(
        Fund, on_delete=models.CASCADE)
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
        return f'{self.admin_code, self.ipsas_code, self.appr_prev, self.actual_prev, self.proposed_curr, self.proposed_next}'


class Revenuedata(models.Model):
    adminCode = models.CharField(max_length=12)
    adminName = models.CharField(max_length=200)
    ipsasCode = models.CharField(max_length=8)
    ecoName = models.CharField(max_length=300)
    fundCode = models.CharField(max_length=5)
    fundName = models.CharField(max_length=200)
    appr = models.DecimalField(default=0.00, max_digits=17, decimal_places=2)
    actual = models.DecimalField(default=0.00, max_digits=17, decimal_places=2)
    prop = models.DecimalField(default=0.00, max_digits=17, decimal_places=2)
