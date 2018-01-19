# -*- coding:utf-8 -*-

#引入需要的模块
import requests

response = requests.get("http://www.baidu.com")
#当不进行编码时，爬取的页面中文出现乱码情况，，进行手动编码
#响应数据编码的设置

response.encoding = "utf-8"
print(response.text)