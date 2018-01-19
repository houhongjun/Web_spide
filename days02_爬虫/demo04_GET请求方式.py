# -*- coding:utf-8 -*-

'''
https://www.baidu.com/s?wd=%E7%81%AB%E8%BD%A6%E7%A5%A8
'''
#引入需要的模块
import urllib2
import urllib
import random

#定义伪装请求的ua
ua = [
    "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
    "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
]

#随机获取一个ua作为身份标识
user_agent = random.choice(ua)

#定义传送的数据
keyword = raw_input("请输入需要搜索的关键词：")
get_param = {
    "wd":keyword
}

#对关键词重新进行编码
data = urllib.urlencode(get_param)

#定义url地址
url = "http://www.baidu.com/s?"
#拼接字符串，---拼接成完整的url路径
full_url = url + data
print (full_url)

#封装请求对象
request = urllib2.Request(full_url)
request.add_header("User-agent",user_agent)

#发送请求得到相应数据
response = urllib2.urlopen(request)

print (response.read())
