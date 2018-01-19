# -*- coding:utf-8 -*-

#引入需要的模块
import requests

#定义POST参数
post_data = {
    "i":"你好",#需要翻译的语句
    "sign":"	08b4f943565560cb69b1cc7d21eda5d7",#加密算法，md5加密
    "salt":"	1515572825815",#---盐值，，时间-毫秒数
    "version	":"2.1",#版本号
    "from":"	AUTO",#词语翻译之前的语言
    "to	":"AUTO",#词语翻译之后的语言
    "smartresult":"	dict",#数据类型
    "typoResult":"	false",#结果类型
    "keyfrom	":"fanyi.web",
    "client	":"fanyideskweb",#客户端标识
    "action	":"FY_BY_REALTIME",#行为描述
    "doctype	":"json",#数据类型
}

#发送请求，得到响应的数据
response = requests.post("http://fanyi.youdao.com",data=post_data)

#打印获取的数据
context = response.text

print(context)

print(type(context))

with open("youdao.html","w") as f:
    f.write("context".encode("utf-8"))

#因为爬取的网页中有汉字内容，但是python2的默认编码不能编码汉字，所以需要我们自己手动进行编码

#保存爬取到的数据到文件--#字符串中，包含了中文，--不能正常的写入文件

# with open("youdao.html","w") as f:
#     f.write(context)
#--错误原因：因为python2中默认调用了context.encode("ascii")出现了编码的错误
#
# 当按照上面的格式写入文件时，会出现如下的错误
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 235-238: ordinal not in range(128)

"""
python3中 s="abc"，默认情况下，s是str类型[unicode]编码
    编码：字符 - > 字节：s.encode("utf-8")
    解码：字节 - > 字符：s.decode("utf-8")
    
python2中 s="abc"，默认情况下，s是str类型[bytes]编码
    编码：字符 - > 字节：s.encode("ascii")
    ---所以需要进行手动编码：字符 - > 字节：s.encode("utf-8")
    解码：字节 - > 字符：s.decode("utf-8") 
    
"""

