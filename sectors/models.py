from django.db import models


class Sector(models.Model):
    sector_code = models.CharField(max_length=12)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
