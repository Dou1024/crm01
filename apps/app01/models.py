from django.db import models


# class UserInfo(models.Model):
#     """
#         创建一张表，表名默认为：前缀 + 类名的小写
#     """
#     name = models.CharField(verbose_name="姓名", max_length=16)
#     age = models.PositiveIntegerField(verbose_name="年龄")
#     create_date = models.DateField(verbose_name="日期", auto_now=True)
#     xcreate_data = models.DecimalField(verbose_name="时间")
#
#     active = models.BooleanField(verbose_name="是否激活")
#     amount = models.DecimalField(verbose_name="余额", max_length=10, decimal_places=2)

class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=16, db_index=True)
    age = models.PositiveIntegerField(verbose_name="年龄")
    email = models.CharField(verbose_name="邮箱", max_length=128, unique=True, null=True)
    amount = models.DecimalField(verbose_name="余额", max_digits=10, decimal_places=2, default=0)
    register_date = models.DateField(verbose_name="注册时间", auto_now=True)


class Goods(models.Model):
    title = models.CharField(verbose_name="标题", max_length=32)
    # detail = models.CharField(verbose_name="详细信息", max_length=255)
    detail = models.TextField(verbose_name="详细信息")
    price = models.PositiveIntegerField(verbose_name="价格")
    count = models.PositiveBigIntegerField(verbose_name="库存", default=0)
