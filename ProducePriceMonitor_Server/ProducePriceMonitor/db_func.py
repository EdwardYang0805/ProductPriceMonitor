import os
from DBModel.models import *
#通过openid获取用户信息
def UserIsExistInDB(open_id):
    user_info = UserInfo.Object.filter(openid=open_id)
    if user_info == None:
        return False
    return True

#添加用户信息
def AddUserInfoToDB(open_id,session):
    info = UserInfo()
    info.openid = open_id
    info.session_key = session
    info.save()

#获取session
def GetUserSession(open_id):
    user_info = UserInfo.Object.filter(openid=open_id)
    return user_info.self_session

#设置session
def SetUserSession(open_id,session_id):
    user_info = UserInfo.Object.filter(openid=open_id)
    user_info.self_session = session_id
    user_info.save()
