import os
import requests
from requests.cookies import RequestsCookieJar

############################################################
#此文件为所有http交互的的接口
############################################################

#发送requests请求
def requestURL(url,header):
    res = requests.get(url, headers=header)
    return res
#下载图片
def downLoadPic_requests(url):
    response = requests.get(url)
    img = response.content
    dir = os.path.abspath('.')
    picpath = os.path.join(dir, 'kaptcha.jpg')
    with open(picpath, 'wb') as f:
        f.write(img)
