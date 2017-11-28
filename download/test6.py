#/usr/bin/env python
#coding:utf-8
#__*__ author: LiuXiankun __*__
'''
download picture
'''

import urllib.request
import random
from  http.cookiejar import CookieJar
import os
import re

def url_open(url):


    headers = {'User-Agent':
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
               }
    req=urllib.request.Request(url, None, headers)
    cj = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    response = opener.open(req)
    html=response.read().decode('utf-8')
    #print(html)
    return html

def get_img(html):
    p = r'<img class="BDE_Image" pic_type="0" width="560" height="840" src="([^"]+\.jpg)"'
    imglist = re.findall(p, html)
    # for each in imglist:
    #     print(each)

    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, filename, None)

if __name__=='__main__':
    url = 'https://tieba.baidu.com/p/5167696089'
    get_img(url_open(url))



