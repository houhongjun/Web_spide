# -*- coding:utf-8 -*-

#引入需要的模块
import scrapy
#导入上级的items模块
from .. import items

class NeiHanSpider(scrapy.Spider):
    """
    内涵段子数据采集爬虫程序
    """
    #定义爬虫名称，用于在命令中调用
    name = "nhspider"
    #定义域名限制：只能爬取----http://neihanshequ.com/域名下的所有数据
    allowed_domains = ["neihanshequ.com"]

    #定义初始url地址---建议使用元组
    start_urls = ('http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1516116999.0 ',)

    def parse(self,response):
        """

        :param response:
        :return:
        """
        print('---*---*---*---*---*---*---*---*---*---*---*---*---*---*---*---')
        import json ,time
        neihan_json = json.loads(response.text)['data']['data']
        # print(neihan_json)
        # print(json.loads(response.text)['data']['data'][1]['group']['content'])

        for i in range(20):
            username = neihan_json[i]['group']['user']['name']
            create_time = neihan_json[i]['group']['create_time']
            create_time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(create_time))
            content = neihan_json[i]['group']['text']

            # print (username)
            # print (create_time)
            # print (content)

            item = items.neihanItem()
            item['username'] = username
            item['createtime'] = create_time
            item['content'] = content

            yield item


