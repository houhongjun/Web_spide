# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

#创建soup对象
soup = BeautifulSoup(open("index.html"),"lxml")

#DOM属性
#1.查询div#container中的所有子标签
print(soup.div.contents)  #获取到子标签列表
print(soup.div.children)  #获取到子标签列表迭代器

for child in soup.div.children:
    print(child)
    print ("-*-" * 10)
    print(child.string)

print(dir(soup))


