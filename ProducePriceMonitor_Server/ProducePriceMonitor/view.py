from django.http import HttpResponse
from . import logic
#搜索商品
def request_seach(request):
    platform = request.GET.get('platform')
    keyword = request.GET.get('keyword')
    print (platform)
    print (keyword)
    return HttpResponse(logic.Do_Seach(platform,keyword))
