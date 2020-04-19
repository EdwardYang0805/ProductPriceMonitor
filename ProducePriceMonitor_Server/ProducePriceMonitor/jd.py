import os
from . import netinterface
from . import const_define
import requests
import time
import re
import json
from lxml import etree

g_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.5,zh;q=0.3',
    'Referer': 'https://www.jd.com/',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'TE': 'Trailers',
}
#京东搜索URL格式：https://search.jd.com/Search?keyword=关键字&enc=utf-8
def Do_Seach(keyword):
    #获取京东平台的搜索地址
    jd_seach_addr = const_define.GetShopSeachAddr("JD")
    if jd_seach_addr == "":
        return const_define.RetNo.Err_NotFoundPlatFormAddr
    #构造搜索URL
    params = (
        ('keyword', keyword),
        ('enc', 'utf-8'),
        ('wq', keyword),
        ('pvid', '70b2126fcf3246ce9f32710d41799ede'),
    )
    res = netinterface.requestURL(jd_seach_addr,g_headers,params)
    print(res.headers)
    if res.status_code != 200:
        return const_define.RetNo.Ret_DoSeachError.value

    print("京东搜索成功")
    res.encoding = 'utf-8'
    goodsList = ParseGoodsInfo(res)
    response = {}
    response["ret"] = "success"
    seach_result ={"platForm": "JD","keyword": keyword}
    seach_result["goodsList"] = goodsList
    response["data"] = seach_result
    return response



#在content中检索商品信息
def ParseGoodsInfo(htmlContent):
    html1 = etree.HTML(htmlContent.text)
    #定位到每一个商品标签li
    datas=html1.xpath('//li[contains(@class,"gl-item")]')
    print(len(datas))
    print(datas)
    jd_goods = []
    for data in datas:
        p_good_id = data.xpath('@data-pid')
        p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
        p_comment = data.xpath('div/div[5]/strong/a/text()')
        p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em')
        p_img = data.xpath('div/div[@class="p-img"]/a/img/@source-data-lazy-img')
            #这个if判断用来处理那些价格可以动态切换的商品，比如上文提到的小米MIX2，他们的价格位置在属性中放了一个最低价
        if len(p_price) == 0:
            p_price = data.xpath('div/div[@class="p-price"]/strong/@data-price')
        print(p_good_id[0] + "    " + p_name[0].xpath('string(.)')+"   "+p_price[0] + "    " + p_img[0])
        #下载图片
        localPath = const_define.GetShopImgPath("JD")
        if localPath == "":
            continue
        netinterface.downLoadPic_requests("https:"+p_img[0],localPath+p_good_id[0]+".png")
        #构造商品信息结构
        goods = {}
        goods["goodsID"] = p_good_id[0]
        goods["goodsName"] = p_name[0].xpath('string(.)')
        goods["goodsPrice"] = p_price[0]
        goods["goodsImg"] = p_img[0]
        jd_goods.append(goods)
       
    return jd_goods


