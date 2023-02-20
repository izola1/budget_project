from django.db import models


class Expenditure(models.Model):
    exp_code = models.CharField(max_length=8)
    description = models.CharField(max_length=300)
    type = models.CharField(max_length=8)

    def __str__(self):
        return self.description
