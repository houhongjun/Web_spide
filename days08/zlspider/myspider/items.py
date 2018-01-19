# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#定义爬取数据组合成对象类型
class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#自定义数据对象类型
class ZhiLianItem(scrapy.Item):
    """
    自定义封装智联招聘的item类型，用于封装采集到的智联网站的数据
    """
    #定义属性字段
    job = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
