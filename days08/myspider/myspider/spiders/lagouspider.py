# -*- coding:utf-8 -*-

#定义需要的scrapy模块
import scrapy
#导入上一级的items模块
from .. import items

class LaGouSpider(scrapy.Spider):
    """
    拉钩招聘数据采集爬虫程序
    """
    #定义爬虫的名称，用于在命令中调用
    name = 'lgspider'

    #定义域名：只能爬取指定域名下的所有数据
    allowed_domains = ["lagou.com"]

    #定义初始url地址---建议使用元组
    start_urls = ("",)
