# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/11 21:51'


from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11'
}

proxies = {
    'https':'219.149.46.151:3129',
    'http':'61.135.217.7:80'
}

url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E6%AD%A6%E6%B1%89&kw=python%E5%B7%A5%E7%A8%8B%E5%B8%88&sm=0&p=1'
response = requests.get(url=url, headers=headers, proxies=proxies)

soup = BeautifulSoup(response.text, 'lxml')

a = soup.select('.zwmc a')
for i in a:
    print(i.string)