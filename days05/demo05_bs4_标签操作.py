# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

#加载构建soup对象
soup = BeautifulSoup(open("index.html"),"lxml")

#备注：bs4通过soup对象直接操作标签：检查文档中是否包含这个标签
#如果要查询文档中的所有指定标签，请使用DOM查询

#1.获取标签对象
#title标签
print(soup.title)   #<title>Xpath测试</title>

#2.操作标签的属性
print ('-*-'*10)
print(soup.h1.attrs)
print(soup.h1.attrs["id"])
print(soup.h1.attrs.get("id"))  #title
print(soup.p.attrs.get("class"))  #None
#通过直接获取标签的方式，获取到匹配成功的第一个标签
print(soup.h2.attrs)#{'id': 'title2'}

#3.操作标签的内容--通过string的方式获取标签的字符串内容
print(soup.h2.string)  #




















