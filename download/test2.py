#/usr/bin/env python
#coding:utf-8
#__*__ author: liuxiankun __*__

'''
download
picture
'''

import urllib.request

url='http://placekitten.com/g/500/400'

req=urllib.request.Request(url)
response=urllib.request.urlopen(req)

picture=response.read()

with open('cat_500_500.jpg','wb') as f:
    f.write(picture)
