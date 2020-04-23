from django.db import models

#用户信息表
class UserInfo(models.Model):
    openid = models.CharField(primary_key=True, max_length=30)
    session_key = models.CharField(max_length=30)
    unionid = models.CharField(max_length=30)
    self_session = models.CharField(max_length=40,default=0)

class UserGoodsInfo(models.Model):
    openid = models.CharField(primary_key=True, max_length=30)
    begin_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)
    platform = models.CharField(max_length=10)
    goods_id = models.CharField(max_length=30)
    monitor_user = models.CharField(max_length=2048)

class GoodsPriceInfo(models.Model):
    goods_id = models.CharField(primary_key=True, max_length=30)
    platform = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now=True)
    price = models.CharField(max_length=15)

class UserMonitorOrder(models.Model):
    order_id = models.CharField(primary_key=True, max_length=30)
    begin_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)
    goods_list = models.CharField(max_length=2048)

class UserMonitorOrderHistory(models.Model):
    order_id = models.CharField(primary_key=True, max_length=30)
    begin_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)
    goods_list = models.CharField(max_length=2048)