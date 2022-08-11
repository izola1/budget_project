from django.db import models
from function_groups.models import Function_Group


class Fund(models.Model):
    group_code = models.ForeignKey(Function_Group, on_delete=models.CASCADE)
    func_code = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.func_code, self.description
