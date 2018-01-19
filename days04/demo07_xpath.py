# -*- coding:utf-8 -*-

"""
//div[@class='upload-txt no-mb']/h1[@class='title']/p
"""
#element tree 节点树
from lxml import etree

html_str = u"""
<html>
    <head>
        <title>文档标题</title>
    </head>

    <body>
        <h1>一级标题<h1>
        <table>
            <tr>
                <th>标题</th>
                <th>标题</th>
                <th>标题</th>
                <th>标题</th>
            </tr>
            <tr>
                <td>内容</td>
                <td>内容</td>
                <td>内容</td>
                <td>内容</td>
            </tr>
        </table>
    </body>
</html>
"""
#html就是一个文档对象，可以直接使用xpath进行数据筛选
html = etree.HTML(html_str)
print (dir(html))

td_value = html.xpath("//td")
#所有的td标签对应的文档对象
print(td_value)
print (dir(td_value))
