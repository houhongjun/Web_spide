# -*- coding:utf-8 -*-

#引入需要的模块
import requests

#定义get参数，---格式是一个字典数据
get_param = {
    "wd":"汽车",
}

#get参数，通过params参数赋值，直接传递该参数值
response = requests.get("http://www.baidu.com/s",params=get_param)

#打印获取的数据
print (response.text)