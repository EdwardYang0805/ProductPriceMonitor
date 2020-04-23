import os
from . import const_define
from . import jd
from . import wx_api
import json
from . import db_func
from DBModel.models import *
session_openid_map = {}
##################################登陆##########################################
def Do_Login(js_code):
    res = wx_api.code2Session(js_code)

    print(res.content)
    if res.status_code == 200:
        print("11")
        res_json = json.loads(res.content)
        if "errcode" in res_json:
            print("22")
            return None
        if db_func.UserIsExistInDB(res_json["openid"]) == False:
            print("33")
            db_func.AddUserInfoToDB(res_json["openid"], res_json["session_key"])
        return res_json["openid"]
    return None
##################################搜索商品 #########################################
def Do_Seach(platform, keyword):
    if platform == 'JD':
        return jd.Do_Seach(keyword)
    else:
        return










