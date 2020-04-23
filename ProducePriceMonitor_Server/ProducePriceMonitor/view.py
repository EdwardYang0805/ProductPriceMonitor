from django.http import HttpResponse
from . import logic
import random
import json
from . import db_func
from datetime import datetime
import time
from django.utils import timezone

#session 有效时间10分钟
session_valid_seconds = 600

#生成随机sessionID
def GetSession():
    res = ''
    for i in range(15):
        num = str(random.randint(1, 9))
        letter = chr(random.randint(65, 90))
        group = random.choice([num, letter])
        res += group
    return res

#校验sessionID的有效性
def checkSessionValid(session_id):
    session_time = db_func.GetSessionLastActiveTime(session_id)
    if session_time == None:
        return False
    cur_time = timezone.now()
    dur_time = (cur_time - session_time).total_seconds()
    print(dur_time)
    if dur_time < session_valid_seconds:
        return True
    else:
        return False

#登陆
def request_login(request):
    ret_json = {}
    res = HttpResponse()
    my_session_id = request.COOKIES.get("my_session_id")
    if checkSessionValid(my_session_id) == False:
        js_code = request.GET.get('code')
        open_id = logic.Do_Login(js_code)
        if open_id == None:
            ret_json["ret"] = "error"
            ret_json["data"] = {"msg": "get user info from wx error"}
            res.write(json.dumps(ret_json))
            res.status_code = 400
            return res
        # 生成自定义session的随机key
        my_session_id = GetSession()
        db_func.SetUserSession(open_id, my_session_id)

    ret_json["ret"] = "success"
    ret_json["data"] = {"my_session_id": my_session_id}
    res.write(json.dumps(ret_json))
    res.status_code = 200
    return res


#搜索商品
def request_seach(request):
    ret_json = {}
    res = HttpResponse()
    my_session_id = request.COOKIES.get("my_session_id")
    if checkSessionValid(my_session_id) == False:
        ret_json["ret"] = "error"
        ret_json["data"] = {"msg": "seseion timeout"}
        res.write(json.dumps(ret_json))
        res.status_code = 301
    else:    
        db_func.UpdateSessionLastActiveTime(my_session_id)
        platform = request.GET.get('platform')
        keyword = request.GET.get('keyword')
        ret_json = logic.Do_Seach(platform,keyword)
        res.write(json.dumps(ret_json))
        res.status_code = 200
        
    return res
