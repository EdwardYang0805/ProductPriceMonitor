from django.http import HttpResponse
from . import logic
import random
import json
from . import db_func
def GetSession():
    res = ''
    for i in range(4):
        num = str(random.randint(1, 9))
        letter = chr(random.randint(65, 90))
        group = random.choice([num, letter])
        res += group
    return res
#登陆
def request_login(request):
    ret_json = {}
    res = HttpResponse()
    js_code = request.GET.get('code')
    open_id = logic.Do_Login(js_code)
    if open_id == None:
        ret_json["ret"] = "error"
        ret_json["data"] = {"msg": "get user info from wx error"}
        res.write(json.dumps(ret_json))
        res.status_code = 400
        return res
    session = db_func.GetUserSession(open_id)
    my_session_id = request.COOKIES.get("my_session_id")
    if session != my_session_id:
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
    platform = request.GET.get('platform')
    keyword = request.GET.get('keyword')
    response = logic.Do_Seach(platform,keyword)
    return HttpResponse(json.dumps(response))
