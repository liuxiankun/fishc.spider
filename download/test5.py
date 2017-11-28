#/usr/bin/env python
#coding:utf-8
#__*__ author: Liu Xiankun __*__
'''
使用代理请求服务器
'''

import urllib.request
import urllib.parse
import random

iplist=['114.215.102.168:8081','121.40.199.105:80','123.103.93.38:80','116.199.2.209:80','116.199.2.210','121.40.213.161:80']
url='http://www.whatismyip.com.tw/'
proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')]
urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')


print(html)





