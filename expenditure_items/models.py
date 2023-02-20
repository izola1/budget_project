from turtle import title
from django.db import models
from expenditures.models import Expenditure


class Expenditure_Item(models.Model):
    exp_code = models.ForeignKey(Expenditure, on_delete=models.CASCADE)
    ipsas_code = models.CharField(max_length=8)
    ipsas_title = models.CharField(max_length=300)

    def __str__(self):
        return self.ipsas_title
