# -*- coding:utf-8 -*-

# 安装bs4
# pip install beautifulsoup4
# easy_install beautifulsoup4
# 下载tar.gz包，pip setup.py install
# 拷贝别人的bs4文件夹，直接复制到site-pakages/目录下即可

#程序中引入了bs4
from bs4 import BeautifulSoup

#加载网页数据
#1.从爬虫获得的网页数据加载
#注意：BeautifulSoup需要指定html解析器---优先使用lxml
soup = BeautifulSoup(open("index.html"),"lxml")

#打印获取的整个网页数据
print(soup)
######################################
#         re       xpath     bs4
#  安装   内置       第三方     第三方
#  语法   正则       路径匹配   面向对象
#  使用   困难       较困难     简单
#  性能   最高       适中       最低
######################################
#PS:因为爬虫程序，一般情况下对于数据处理性能问题涉及较少，
#所以，对于爬虫采集数据、筛选数据并没有性能要求！[时间上比较充裕]