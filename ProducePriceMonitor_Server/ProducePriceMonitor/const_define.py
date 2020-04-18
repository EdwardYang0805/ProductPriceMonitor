import os
from enum import Enum
#电商平台首页地址
const_shop_base_addr = [{"name":"JD","addr":"https://www.jd.com"}]
#电商平台搜索地址
const_shop_seach_addr=[{"name":"JD","addr":"https://search.jd.com/Search"}]
#商品图片保存路径
const_shop_goods_img_path = [{"name":"JD","path":"img/jd/goods_img/"}]
class RetNo(Enum):
    Ret_Success = 0
    Ret_NotFoundPlatFormAddr = 1        #未找到该平台的搜索地址
    Ret_DoSeachError = 2                #向平台进行搜索返回失败

def GetShopSeachAddr(platformName):
    for addrinfo in const_shop_seach_addr:
        if addrinfo["name"] == platformName:
            return addrinfo["addr"]
    return ""

def GetShopImgPath(platformName):
    for path in const_shop_goods_img_path:
        if path["name"] == platformName:
            return path["path"]
    return ""
