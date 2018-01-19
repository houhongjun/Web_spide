# -*- coding:utf-8 -*-
import urllib2

import ssl

#创建一个忽略警告的上下文对象
context = ssl._create_unverified_context()

request = urllib2.Request("https://www.12306.cn")

response = urllib2.urlopen(request,context=context)

print response.read()
#urllib2.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:661)>