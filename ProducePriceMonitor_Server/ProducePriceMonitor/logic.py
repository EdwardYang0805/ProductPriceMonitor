import os
from . import const_define
from . import jd
from . import wx_api
##################################登陆##########################################
def Do_Login(js_code):
    res = wx_api.code2Session(js_code)
    if res.status_code == 200:
        #绑定session
        ret_json = {"ret": "success"}
        ret_json["data"] = {"session": "111111111"}
    else:
        ret_json = {"ret": "loginFail"}
    return ret_json
##################################搜索商品 #########################################
def Do_Seach(platform, keyword):
    if platform == 'JD':
        return jd.Do_Seach(keyword)
    else:
        return










