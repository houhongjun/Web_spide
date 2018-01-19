# -*- coding:utf-8 -*-

# 引入需要的模块
import urllib2

# 定义请求对象
requset = urllib2.Request("http://www.baidu.com/damu")

# 使用try-except包裹请求
try:
    response = urllib2.urlopen(requset)
    print(response.read())
except Exception, err:
    print err.code
    print err

print("程序运行完成")

