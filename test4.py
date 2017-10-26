#/usr/bin/env python
#coding:utf-8
#__*__ author: Liu Xiankun __*__
'''

'''

import urllib.request
import urllib.parse
import json
import time

'''
1.模拟浏览器，自己构造header
2.设置提交时间
3.使用代理

head={
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
'''


url ='http://fanyi.youdao.com/translate?'
#url ='http://fanyi.youdao.com/'


while True:
    content = input('请输入需要翻译的内容(wq!退出)：')
    if content=='wq!':
        break

    data={
    'i':content,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1506221550086',
    'sign':'d930773d68e0935e4a5781f3a187e62f',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_CLICKBUTTION',
    'typoResult':'true'
    }
    data=urllib.parse.urlencode(data).encode('utf-8')

    req=urllib.request.Request(url,data)

    response=urllib.request.urlopen(req)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    html=response.read().decode('utf-8')
    target=json.loads(html)
    print('翻译结果:%s'%(target['translateResult'][0][0]['tgt']))
    time.sleep(5)
