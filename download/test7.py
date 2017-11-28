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
    p = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
    iplist = re.findall(p, html)

    for each in iplist:
        print(each)

if __name__=='__main__':
    url = 'http://www.xicidaili.com/'
    get_img(url_open(url))



