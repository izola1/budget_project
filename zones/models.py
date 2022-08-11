from django.db import models


class Zone(models.Model):
    zone_code = models.CharField(max_length=4, unique=True)
    zone = models.CharField(max_length=255)

    def __str__(self):
        return self.zone_code, self.zone
