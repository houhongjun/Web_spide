# -*- coding:utf-8 -*-
#第一行注释，为了让源代码能够支持中文

#引入需要的模块
import requests

#发送请求得到相应数据
response = requests.get("https://www.taobao.com")


#打印展示获取的数据
print (response.text)
