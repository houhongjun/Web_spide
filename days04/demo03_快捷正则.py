# -*- coding:utf-8 -*-

#引入正则表达式操作模块
import re

#定义一个正则表达式
regexp = r"\d+"



# 定义目标字符串
intro = "laomu jinnian 22 le! lao le lao le!"

#匹配得到的数据
v_list = re.findall(regexp,intro)

print (v_list)