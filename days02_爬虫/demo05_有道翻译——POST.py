# -*- coding:utf-8 -*-

"""
访问url:http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
请求参数：
    i = bird
    from=AUTO
    to = AUTO
    smartresult = dict
    client = fanyideskweb
    salt = 1515474100878
    sign = 479264ddd0ccaed172916c479c3fd30d
    doctype = json
    version = 2.1
    keyfrom = fanyi.web
    action = FY_BY_REALTIME
    typoResult = false
"""
#引入需要的模块
import urllib2
import urllib
import random
import json


import time
E = "fanyideskweb"
#salt盐值
r = str(time.time()*1000)
#确定翻译的数据
n = raw_input("请输入需要翻译的词语：")
#确定加密的混淆码
O = "aNPG!!u6sesA>hBAW1@(-"
#确定sign参数
import hashlib
sign = hashlib.md5(E + n + r + O).hexdigest()

#设置有道在线翻译的请求头
headers = {
    #"Host": "fanyi.youdao.com",
    #"Connection": "keep-alive",
    #"Content-Length": "200",
    #"Accept": "application/json, text/javascript, */*; q=0.01",
    #"Origin": "http://fanyi.youdao.com",
    #"X-Requested-With": "XMLHttpRequest",
    #"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http://fanyi.youdao.com/",
    # "Accept-Encoding": "gzip, deflate",
    #"Accept-Language": "zh-CN,zh;q=0.8",
    "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=2075764580.1728754; OUTFOX_SEARCH_USER_ID=-995280811@10.168.8.63; JSESSIONID=aaaxakcpWa-oo8wK72ydw; fanyi-ad-id=39535; fanyi-ad-closed=1; ___rl__test__cookies=1515468614442i=hell&from=AUTO&to=AUTO&smartresult=dict&client=fanyideskweb&salt=1515468614446&sign=710df1dcc70f91c1b04e795a34704c8e&doctype=json&version=2.1&keyfrom=fanyi.web&action=FY_BY_REALTIME&typoResult=false"
}

#定义ua

ua = [
    "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
    "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
]

#随机获取一个ua
user_agent = random.choice(ua)

#定义url地址

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

#定义表单数据
form_data = {
    "i" : n,   #需要翻译的内容
    "from": "AUTO",
    "to": "AUTO",
    "smartresult" : "dict",
    "client" : "fanyideskweb",
    "salt" :  r,
    "sign" : sign,
    "doctype" : "json",
    "version" : 2.1,
    "keyfrom" : "fanyi.web",
    "action" : "FY_BY_REALTIME",
    "typoResult" : False
}

data = urllib.urlencode(form_data)


#封装请求对象
request = urllib2.Request(url,data=data,headers=headers)
request.add_header("User-agent",user_agent)


#发送请求获取响应数据
response = urllib2.urlopen(request)

#打印展示数据
result = response.read()
# result = result['translateResult'][0][0]['tgt']

# print ("翻译的结果为：%s" % result['translateResult'][0][0]['tgt'])


translation = json.loads(result)

#UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 0: ordinal not in range(128)---出现错误
#解决办法：在需要输出的内容之前加'u'----标识其为utf-8编码格式
print (u'翻译的结果为：%s'%translation['translateResult'][0][0]['tgt'])
