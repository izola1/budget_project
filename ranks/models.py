from django.db import models
from sectors.models import Sector


class Rank(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.DO_NOTHING)
    gl = models.CharField(max_length=12)
    rank = models.CharField(max_length=200)

    def __str__(self):
        return self.sector, self.gl, self.rank
