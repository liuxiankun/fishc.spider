#/usr/bin/env python
#coding:utf-8
#__*__ author: LiuXiankun __*__
'''
download picture
'''

import urllib.request
import random
from http.cookiejar import CookieJar
import os
import re


def url_open(url):

    '''
    请求一个网址，返回页面信息
    :param url:
    :return:
    '''

    #设置代理
    iplist = ['114.215.102.168:8081', '121.40.199.105:80', '123.103.93.38:80', '116.199.2.209:80', '116.199.2.210',
              '121.40.213.161:80']
    proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})

    open = urllib.request.build_opener(proxy_support)

    open.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')]
    urllib.request.install_opener(open)



    headers = {'User-Agent':
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
               }

    #建立有cookie的请求
    #在 HTTP Request 中加入特定的 Header 要加入 header，需要使用 Request 对象：

    request = urllib.request.Request(url, None, headers)
    cj = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    response = opener.open(request)
    html=response.read()
    #print(url)
    return html


def get_page(url):
    html = url_open(url).decode('utf-8')
    p=re.compile(r'<span class="current-comment-page">\[(\d+)\]</span>')
    page_num=re.findall(p,html)
    #print(page_num[0])
    #<span class="current-comment-page">[231]</span>
    return page_num[0]


def find_imgs(url):
    html=url_open(url).decode('utf-8')
    p = r'<img src="(//(?:[^"]+)\.jpg)"'
    imglist = re.findall(p, html)
    # for each in imglist:
    #     print('http:'+each)

    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve('http:'+each, filename, None)


def download_mm(folder, pages=3):
    if not os.path.exists(folder):
        os.system('mkdir %s'%folder)
    os.chdir(folder)
    url="http://jandan.net/ooxx/"
    get_page(url)

    page_num=int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url=url+'page-'+ str(page_num)+ '#comments'
        find_imgs(page_url)

if __name__=='__main__':

    download_mm('picture',10)



