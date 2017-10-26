#/usr/bin/env python
#coding:utf-8
#__*__ author: liuxiankun __*__
'''
请求网页
下载图片
'''

import urllib.request

url='http://www.fishc.com'
req=urllib.request.Request(url)
response=urllib.request.urlopen(req)

html=response.read().decode()

print(html)

