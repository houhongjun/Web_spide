# -*- coding:utf-8 -*-

"""
simple spider
"""
#引入需要的模块
import urllib2

#访问目标网站，获取网站的响应数据
response = urllib2.urlopen('https://www.taobao.com')

#打印获取到的数据，获取到的数据，包含在响应对象的read()函数中可以访问
#--python2--第一种打印方式
# print(response.read())

#--python2---第二种打印方式
print response.read()



