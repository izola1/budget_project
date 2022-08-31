from django.db import models


class Function_Group(models.Model):
    group_code = models.CharField(max_length=4, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.group_code} {self.description}'
