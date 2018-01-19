# -*- coding:utf-8 -*-

"""
cookie基本操作
"""
#引入需要的模块
import urllib2
import cookielib

#创建一个cookie核心对象
cookie = cookielib.CookieJar()

#创建一个自定义的Handler对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

#创建一个可以操作cookie的opener对象
cookie_opener = urllib2.build_opener(cookie_handler)

#定义访问url地址和请求对象
url = "https://www.baidu.com"
request = urllib2.Request(url)

#发送一个请求
response = cookie_opener.open(request)


#####此段程序重点不在于获取到什么数据，而在于cookie中出现了什么数据

for item in cookie:
    print ("%s-*-%s" %(item.name,item.value))

    #在python2中占位符有两种形式：
    # print ("{}-*-*-{}".format(item.name,item.value))

