# -*- coding:utf-8 -*-

import urllib2

url = "https://www.taobao.com"

#根据url地址构建一个请求对象
request = urllib2.Request(url)


#通过Urlopen()函数发送这个请求，得到服务器的响应数据
response = urllib2.urlopen(request)

#打印输出得到的数据
print (response.read())