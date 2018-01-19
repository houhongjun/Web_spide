# -*- coding:utf-8 -*-

"""
urllib2模块是爬虫操作的底层模块，但不是程序编码的底层代码
"""
import urllib2

response = urllib2.urlopen("https://www.taobao.com")

print(response.read())