from django.db import models
from mdas.models import Mda
# from economic_groups.models import Economic_Group
# from economic_items.models import Economic_Item
# from expenditure_items.models import Expenditure_Item
# from rev_groups.models import Rev_Group
from revenue_items.models import Revenue_Item
from funds.models import Fund


class Capital_Receipt(models.Model):
    admin_code = models.ForeignKey(Mda, on_delete=models.CASCADE)
    # ipsas_code = models.ForeignKey(Expenditure_Item, on_delete=models.CASCADE)
    ipsas_code = models.ForeignKey(Revenue_Item, on_delete=models.CASCADE)
    # eco_code = models.ForeignKey(Rev_Group, on_delete=models.CASCADE)
    fund_code = models.ForeignKey(Fund, on_delete=models.CASCADE)
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
        # return self.admin_code, self.ipsas_code, self.appr_prev, self.actual_prev, self.proposed_curr
        return f'{self.admin_code} {self.ipsas_code} {self.appr_prev} {self.actual_prev} {self.proposed_curr}'
