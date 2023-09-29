from django.db import models


class Role(models.Model):
    """
        创建一张表，表名默认为：前缀 + 类名的小写
    """
    name = models.CharField(max_length=16)
    age = models.IntegerField()

