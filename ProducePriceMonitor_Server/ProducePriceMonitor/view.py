from django.http import HttpResponse
from . import logic
import json
#登陆
def request_login(request):
    js_code = request.GET.get('code')
    ret_content = logic.Do_Login(js_code)
    res = HttpResponse()
    if res["ret"] == "success":
        res.status_code = 200
    else:
        res.status_code = 400
    res.write(ret_content)
#搜索商品
def request_seach(request):
    platform = request.GET.get('platform')
    keyword = request.GET.get('keyword')
    response = logic.Do_Seach(platform,keyword)
    return HttpResponse(json.dumps(response))