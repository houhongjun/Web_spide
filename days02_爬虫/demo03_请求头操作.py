# -*- coding:utf-8 -*-

"""
为了对抗反爬虫机制，需要将我们的爬虫程序，伪装成浏览器发送请求
1.定义User-agent
2.设置请求头

重点内容：请求头的设置
    请求头中的数据可以被重新设置
    请求头中可以传送自定义数据
"""
#导入爬虫操作的底层模块
import urllib2

import random
#定义可用的user-agent
ua = [
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.5) Gecko/20041108 Firefox/1.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.55 Safari/525.19 ",
]
#随机获取user-agent
user_agent = random.choice(ua)
print user_agent

#定义请求头
my_header = {
    "User-agent":user_agent,
    "message":"hello"
}

#封装请求对象，并且设置请求头数据
url = "https://www.baidu.com"
request = urllib2.Request(url,headers=my_header)

#发送请求并且获取数据
response = urllib2.urlopen(request)

print (response.read())


