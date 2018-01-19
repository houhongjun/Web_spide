# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/16 19:20'

import scrapy
from .. import items

class neihanSpider(scrapy.Spider):
    # 在命令行被调用的名称
    name = 'nhspider'
    # 限制只爬取这个域名下的数据
    allowed_domains = ['neihanshequ.com']
    # 爬取的url地址
    start_urls = (
        'http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1516101542.0',
    )

    def parse(self, response):
        print('********************************************')
        import json, time
        neihan_json = json.loads(response.text)['data']['data']
        # print(neihan_json)
        # print(json.loads(response.text)['data']['data'][0]['group']['text'])
        for i in range(20):
            username = neihan_json[i]['group']['user']['name']
            create_time = neihan_json[i]['group']['create_time']
            createtime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(create_time))
            content = neihan_json[i]['group']['text']

            # print username
            # print create_time
            # print content

            item = items.neihanItem()
            item['username'] = username
            item['createtime'] = createtime
            item['content'] = content

            yield item








