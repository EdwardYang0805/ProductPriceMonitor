import os
from . import const_define
from . import jd

##################################搜索商品 #########################################
def Do_Seach(platform,keyword):
    if platform == 'JD':
        return jd.Do_Seach(keyword)
    else:
        return










