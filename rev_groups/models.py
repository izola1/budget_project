from django.db import models


class Rev_Group(models.Model):
    eco_code = models.CharField(max_length=6, unique=True)
    group_title = models.CharField(max_length=255)

    # def type_default():
    #     return {"name": "not_provided"}

    group_type = models.CharField(max_length=255, blank=True,)

    def __str__(self):
        return f'{self.eco_code} {self.group_title}'
