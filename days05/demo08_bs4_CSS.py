# -*- coding:utf-8 -*-

"""
BeautifulSoup4
>理论基础：[爬虫程序--性能的要求、时间的限制]相对较弱
>DOM操作：参考JavaScript--DOM操作属性和函数[面试较多]

>css操作：参考css语法：--项目实际操作较多，但是面试基本问题不多
？？--在你的爬虫项目中，使用过BS4吗？
-----用过，经常用，一般用他的select函数直接操作来完成数据筛选！
？？--那你用过他的DOM操作吗？？
-----偶尔用过，它的DOM结构树的数据查询，和JavaScript中的DOM操作有点类似
------在用的时候更加灵活，可以操作的参数可以是名称、可以是正则，所以有些时候会用到
？？--什么时候会用到呢？
-----我没有用过，但我的同事用过，我给改成了css，
-----因为两种操作方式对于性能处理来说并没有特别好的提升，但css语法相对于DOM筛选的可读性更好

JSONPath->针对json数据进行结构化匹配的描述语言，类似xpath

"""

#引入bs4
from bs4 import BeautifulSoup

#加载文档，构建soup DOM对象
soup = BeautifulSoup(open("index.html"),"lxml")

#CSS操作，核心操作函数：select()
#1.标签选择器
span_e = soup.select("span")
print(span_e)

#2.ID选择器
h1_id = soup.select("#title")
print(h1_id)
print(h1_id[0].string)

#3.class 选择器
p_class = soup.select(".content")
print(p_class)
print(p_class[0].string)

#4.包含选择器
p_e = soup.select("#container p")
print(p_e)
print(p_e[0].string)


#5.子类选择器
p_k = soup.select("#container p")
print (p_k)

#6.属性选择器
div_attr = soup.select("div[class]")
print (div_attr)

div_attr2 = soup.select("div[id='intro']")
print(div_attr2)
