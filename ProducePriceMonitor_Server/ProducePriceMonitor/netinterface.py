import os
import requests
from requests.cookies import RequestsCookieJar

############################################################
#此文件为所有http交互的的接口
############################################################

#发送requests请求
def requestURL(url,header,params):
    res = requests.get(url, headers=header,params=params)
    return res
#下载图片
def downLoadPic_requests(url,local_name):
    response = requests.get(url)
    img = response.content
    dir = os.path.abspath('.')
    picpath = os.path.join(dir, local_name)
    with open(picpath, 'wb') as f:
        f.write(img)
