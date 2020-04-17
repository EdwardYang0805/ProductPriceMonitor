import os
from . import netinterface
from . import const_define
import requests
from lxml import etree
import time

g_headers = {'referer': 'https://search.jd.com',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
#京东搜索URL格式：https://search.jd.com/Search?keyword=关键字&enc=utf-8
def Do_Seach(keyword):
    #获取京东平台的搜索地址
    jd_seach_addr = const_define.GetShopSeachAddr("JD")
    if jd_seach_addr == "":
        return const_define.RetNo.Err_NotFoundPlatFormAddr
    #构造搜索URL
    strURL = jd_seach_addr + "？keyword=" + keyword + "&enc=utf-8"
    res = netinterface.requestURL(strURL,g_headers)
    print(res.headers)
    if res.status_code != 200:
        return const_define.RetNo.Ret_DoSeachError.value

    print("京东搜索成功")
    #res.encoding = 'utf-8'
    ParseGoodsInfo(res)
    return const_define.RetNo.Ret_Success.value



#在content中检索商品信息
def ParseGoodsInfo(htmlContent):
    html1 = etree.HTML(htmlContent.text)
    print(html1)
    datas = html1.xpath('//li[contains(@class,"gl-item")]')
    print(datas)

