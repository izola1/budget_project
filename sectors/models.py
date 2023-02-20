from django.db import models


class Sector(models.Model):
    sector_code = models.CharField(max_length=12, default="000000000000")
    sector_name = models.CharField(max_length=200)

    def __str__(self):
        return self.sector_name
