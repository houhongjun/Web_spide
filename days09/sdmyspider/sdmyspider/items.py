# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SdmyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ZhilinaItem(scrapy.Item):
    """
    智联数据采集包装类型
    """
    #定义属性字段
    job_name = scrapy.Field()