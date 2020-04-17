from django.http import HttpResponse
from . import logic
#搜索商品
def request_seach(request):
    profrom = request.GET.get('profrom')
    produce = request.GET.get('produce')
    print (profrom)
    print (produce)
    return HttpResponse(logic.Do_Seach(profrom,produce))
