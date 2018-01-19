# -*- coding:utf-8 -*-

import urllib2

#英雄联盟第一页数据url地址
url = "https://tieba.baidu.com/f?kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&ie=utf-8&pn=0"

response = urllib2.urlopen(url)

content = response.read()

print(content)

with open("1.html",'w') as f:
    f.write(content)
