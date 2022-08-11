from django.db import models


class Fund_Group(models.Model):
    group_code = models.CharField(max_length=3, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.group_code, self.description
