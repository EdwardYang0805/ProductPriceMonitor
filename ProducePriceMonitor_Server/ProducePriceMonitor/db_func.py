import os
from DBModel.models import *
from datetime import datetime
from django.utils import timezone
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

