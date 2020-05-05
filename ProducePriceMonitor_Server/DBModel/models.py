from django.db import models

#用户信息表
class UserInfo(models.Model):
    openid = models.CharField(primary_key=True, max_length=30)
    session_key = models.CharField(max_length=30)
    unionid = models.CharField(max_length=30)
    self_session = models.CharField(max_length=40,default=0)
    last_active_time = models.DateTimeField(auto_now=True)

class MonitorGoodsInfo(models.Model):
    goods_id = models.CharField(primary_key=True, max_length=30)
    begin_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField()
    goods_price = models.CharField(max_length=10240, default="")

class GoodsPriceInfo(models.Model):
    goods_id = models.CharField(primary_key=True, max_length=30)
    platform = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now=True)
    price = models.CharField(max_length=15)

class UserMonitorCart(models.Model):
    openid = models.CharField(primary_key=True, max_length=30)
    goods_list = models.CharField(max_length=2048)

class UserMonitorOrder(models.Model):
    openid = models.CharField(max_length=30)
    order_id = models.AutoField(primary_key=True)
    begin_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)
    goods_list = models.CharField(max_length=2048)
    finished = models.BooleanField(default=False)