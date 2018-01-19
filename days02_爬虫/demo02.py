# -*- coding:utf-8 -*-

import urllib2

url =  "https://www.taobao.com"
request = urllib2.Request(url)

response = urllib2.urlopen(request)

print response.read()
