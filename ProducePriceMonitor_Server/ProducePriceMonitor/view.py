from django.http import HttpResponse
from . import logic
import json
#登陆
def request_login(request):
    js_code = request.GET.get('code')
    logic.Do_Login(js_code)

#搜索商品
def request_seach(request):
    platform = request.GET.get('platform')
    keyword = request.GET.get('keyword')
    response = logic.Do_Seach(platform,keyword)
    return HttpResponse(json.dumps(response))
