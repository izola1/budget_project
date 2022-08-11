from django.db import models
from zones.models import Zone


class Location(models.Model):
    zone_code = models.ForeignKey(Zone, on_delete=models.CASCADE)
    loc_code = models.CharField(max_length=8, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.group_code, self.description
