import os
from enum import Enum
const_shop_base_addr = [{"name":"JD","addr":"https://www.jd.com"}]
const_shop_seach_addr=[{"name":"JD","addr":"https://search.jd.com/Search"}]

class RetNo(Enum):
    Ret_Success = 0
    Ret_NotFoundPlatFormAddr = 1        #未找到该平台的搜索地址
    Ret_DoSeachError = 2                #向平台进行搜索返回失败

def GetShopSeachAddr(platformName):
    for addrinfo in const_shop_seach_addr:
        if addrinfo["name"] == platformName:
            return addrinfo["addr"]
    return ""
