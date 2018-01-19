# -*- coding:utf-8 -*-

"""
Xpath : python通过lxml模块进行操作
"""
#用于进行DOM树对象转换的模块
from lxml import etree

#从文件中加载html文档数据
html = etree.parse("index.html")

#爬虫--直接获取得到的数据
#节点树模型 -> dom树模型
print(html) #<lxml.etree._ElementTree object at 0x0000000004CE8108>

#1.获取数据：直接操作标签
ele_h1 = html.xpath("//h1")
print(ele_h1)#[<Element h1 at 0x4e18088>] h1节点对象
print(ele_h1[0].xpath("string(.)"))#获取h1标签的内容 登黄鹤楼
print(ele_h1[0].text)#获取h1标签的内容 登黄鹤楼

#2.获取数据···操作标签的属性
ele_h2_csb = html.xpath("//h2[@id='title2']")
print(ele_h2_csb)   #[<Element h2 at 0x5728048>]
print(ele_h2_csb[0].text)   #得到对象中的数据----出师表

ele_h2_zgl = html.xpath("//h2[@id='intro_title']")
print(ele_h2_zgl)  #[<Element h2 at 0x5574fc8>]
print (ele_h2_zgl[0].text)   #诸葛亮
print (ele_h2_zgl[0].xpath("string(.)"))   #诸葛亮 孔明


#3.通过属性执行获取标签对象
#获取body下面所有p标签
# ele_p_dhhl = html.xpath("//body//p[@class='content']")

#获取body下面所有p标签
ele_p_dhhl = html.xpath("//body/p[@class='content']")
print(ele_p_dhhl)

for ele_p in ele_p_dhhl:
    print(ele_p.text)

print("-*-"*10)
ele_p_dhhl = html.xpath("//body/p[@class='content'][1]")

print(ele_p_dhhl[0].text)
print (type(ele_p_dhhl))#<type 'list'>