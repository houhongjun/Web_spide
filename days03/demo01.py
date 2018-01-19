# -*- coding:utf-8 -*-
#为了源代码中能够支持中文

#引入需要的模块
import requests

#发送请求得到响应数据
response = requests.get("http://www.taobao.com")

#打印展示获取的数据

print (response.text)