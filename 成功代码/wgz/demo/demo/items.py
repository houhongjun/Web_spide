# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class zhilianItem(scrapy.Item):
    '''
    自定义封装智联招聘的item类型，用于封装采集到的之恋网站的数据
    '''
    # 定义属性字段
    job = scrapy.Field()
    company = scrapy.Field()
    money = scrapy.Field()


class neihanItem(scrapy.Item):
    username = scrapy.Field()
    createtime = scrapy.Field()
    content = scrapy.Field()
