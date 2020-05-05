import os
from DBModel.models import *
from datetime import datetime
from django.utils import timezone
import json
#通过openid获取用户信息
def UserIsExistInDB(open_id):
    try:
        user_info = UserInfo.objects.get(openid=open_id)
        print(user_info)
    except UserInfo.DoesNotExist:
        print("no")
        return False
    else:
        return True

#添加用户信息
def AddUserInfoToDB(open_id,session):
    info = UserInfo()
    info.openid = open_id
    info.session_key = session
    info.save()

#获取session
def GetUserSession(open_id):
    try:
        user_info = UserInfo.objects.get(openid=open_id)
    except UserInfo.DoesNotExist:
        print("nohave")
        return 0
    else:
        print(user_info.self_session)
        return user_info.self_session

#设置session
def SetUserSession(open_id,session_id):
    try:
        user_info = UserInfo.objects.get(openid=open_id)
    except UserInfo.DoesNotExist:
        return 
    else:
        user_info.self_session = session_id
        user_info.last_active_time = timezone.now()
        user_info.save()
#获取上一次活跃时间
def GetSessionLastActiveTime(session_id):
    try:
        user_info = UserInfo.objects.get(self_session=session_id)
    except UserInfo.DoesNotExist:
        return None
    else:
        return user_info.last_active_time
#更新活跃时间
def UpdateSessionLastActiveTime(session_id):
    try:
        user_info = UserInfo.objects.get(self_session=session_id)
    except UserInfo.DoesNotExist:
        return
    else:
        user_info.last_active_time = timezone.now()
        user_info.save()
#通过seesion获取用户openid
def GetUserOpenIdBySeesion(session_id):
    try:
        user_info = UserInfo.objects.get(self_session=session_id)
    except UserInfo.DoesNotExist:
        return None
    else:
        return user_info.openid
#获取用户检测车商品列表
def GetUserMonitorCartGoodsList(openID):
    try:
        cart_info = UserMonitorCart.objects.get(openid=openID)
    except UserMonitorCart.DoesNotExist:
        return None
    else:
        return json.loads(cart_info.goods_list)
#向用户监测车中添加商品
def UpdateGoodsToMonitorCart(openID,goods_list_obj):
    try:
        cart_info = UserMonitorCart.objects.get(openid=openID)
    except UserMonitorCart.DoesNotExist:
        cart_info = UserMonitorCart()
        cart_info.openid = openID
        cart_info.goods_list = json.dumps(goods_list_obj)
    else:
        cart_info.goods_list = json.dumps(goods_list_obj)
    cart_info.save()

#添加一个订单
def AddMonitorOrder(openID,order_json_obj):
    print(order_json_obj)
    order_info =UserMonitorOrder()
    order_info.openid = openID
    order_info.begin_time =timezone.now()
    order_info.end_time = order_json_obj['endTime']
    order_info.finished = False
    goodsListsJson = {}
    goodsListsJson["goodsList"] = order_json_obj['goodsList']
    order_info.save()

#添加监测商品
def AddMonitorGoods(end_time,good_info):
    try:
        print("2222222222222222222222222222")
        goods_info = MonitorGoodsInfo.objects.get(goods_id =good_info['goodsid'])
        print("333333333333333333333333333333")
    except MonitorGoodsInfo.DoesNotExist:
        goods_info = MonitorGoodsInfo()
        goods_info.goods_id = good_info['goodsid']
        goods_info.begin_time = timezone.now()
        goods_info.end_time = end_time;
        print(end_time)
        goods_info.save()
    else:
        goods_info.end_time = end_time
        goods_info.save



