import os
from . import const_define
from . import jd

##################################搜索商品 #########################################
def Do_Seach(proformName,produceid):
    if proformName == 'JD':
        return jd.Do_Seach(produceid)
    else:
        return










