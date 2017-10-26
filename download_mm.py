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


def url_open(url):
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
    req=urllib.request.Request(url, None, headers)
    cj = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    response = opener.open(req)
    html=response.read()
    #print(url)
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']',a)
    #print(html[a:b])

    return html[a:b]


def find_imgs(url):
    html=url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while a!=-1:
        b=html.find('.jpg', a, a+255)
        if b!=-1:
            img_addrs.append(html[a+9:b+4])
        else:
            b= a+9

        a=html.find('img src=',b)

    # for each in img_addrs:
    #     print(each)
    return img_addrs

def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename=each.split('/')[-1]
        with open(filename, 'wb') as f:
            img=url_open('http:'+each)
            f.write(img)
def download_mm( folder, pages=10 ):
    os.mkdir(folder)
    os.chdir(folder)

    url="http://jandan.net/ooxx/"
    page_num=int(get_page(url))
    #print('hello world')

    for i in range(pages):
        page_num -= i
        page_url=url+'page-'+ str(page_num)+ '#comments'
        img_addrs=find_imgs(page_url)
        save_imgs(folder,img_addrs)
if __name__=='__main__':

    download_mm('picture2',10)



