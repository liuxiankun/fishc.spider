#/usr/bin/env python
#coding:utf-8
#__*__ author: liuxiankun __*__
'''
有道翻译
'''


import urllib.request
import urllib.parse
import json


url ='http://fanyi.youdao.com/translate?'
#url ='http://fanyi.youdao.com/'
content=input('请输入需要翻译的内容：')

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

response=urllib.request.urlopen(url,data)
html=response.read().decode('utf-8')
target=json.loads(html)
print('翻译结果:%s'%(target['translateResult'][0][0]['tgt']))




