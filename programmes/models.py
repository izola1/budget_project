from django.db import models


class Programme(models.Model):
    code = models.CharField(max_length=2, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.code} {self.description}'
