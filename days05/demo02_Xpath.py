# coding:utf-8

"""
Xpath：python通过lxml模块进行操作
"""
#用于进行DOM对象转换的模块
from lxml import etree

#从文件中加载html文档数据
html = etree.parse("index.html")

#爬虫··直接获取到的数据
print(html)   #<lxml.etree._ElementTree object at 0x0000000005058108>

#1.获取数据：直接操作标签
ele_h1 = html.xpath("//h1")
print (ele_h1)#[<Element h1 at 0x5b28088>] h1节点对象
print(ele_h1[0].xpath("string(.)"))#登黄鹤楼
print(ele_h1[0].text)#登黄鹤楼

#2.获取数据··操作标签的属性
ele_h2_csb = html.xpath("//h2[@id='title2']")
print (ele_h2_csb)#[<Element h2 at 0x5178048>]
print(ele_h2_csb[0].text)#出师表

ele_h2_zgl = html.xpath("//h2[@id='intro_title']")
print (ele_h2_zgl)#[<Element h2 at 0x52a4fc8>]
print (ele_h2_zgl[0].text)#诸葛亮 ---两者有明显的不同，text只能打印其中的一部分内容
print (ele_h2_zgl[0].xpath("string(.)"))#诸葛亮 孔明--打印所有的内容

#3.通过属性执行获取标签对象
# ele_p_dhhl = html.xpath("//body//p[@class='content']")# 获取body下面所有p标签
#获取body下面所有p标签
ele_p_dhhl = html.xpath("//body/p[@class='content']")

print(ele_p_dhhl)
print ("^^^^"*10)
for ele_p in ele_p_dhhl:
    print (ele_p.text)

#获取body下面所有p标签
ele_p_dhhl = html.xpath("//body/p[@class='content'][1]")

print (ele_p_dhhl[0].text)