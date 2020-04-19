import os
import requests
from . import const_define
def code2Session(js_code):
    params = (
        ('appid', const_define.AppID),
        ('secret', const_define.AppSecret),
        ('js_code', js_code),
        ('grant_type', 'authorization_code'),
    )
    res = requests.get("https://api.weixin.qq.com/sns/jscode2session", params=params)
    return res