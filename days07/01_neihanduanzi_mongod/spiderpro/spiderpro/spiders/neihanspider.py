# -*- coding:utf-8 -*-

#引入需要的模块
import scrapy
#导入上一级的items模块
from .. import items

class NeiHanSpider(scrapy.Spider):
    """
    内涵段子数据采集爬虫程序
    """
    #定义爬虫程序的名称
    name = "nhspider"
    #定义域名限制
    allowed_domains = ["neihanshequ.com"]

    #定义初始url地址---建议使用元组
    start_urls = ("http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1516141310 ",)

        # print(response.body)
        # filename = response.url.split("&")[-1] + ".html"
        # with open(filename,"w") as f:
        #     f.write(response.body)
    def parse(self,response):
        print('---*---*---*---*---*---*---*---*---*---*---*---*---*---*---*---')
        import json,time
        neihan_json = json.loads(response.text)['data']['data']
        # print (neihan_json)

        for i in range(20):
            username = neihan_json[i]['group']['user']['name']
            create_time = neihan_json[i]['group']['create_time']
            create_time = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(create_time))
            content = neihan_json[i]['group']['content']

            # print (username)
            # print (create_time)
            # print (content)

            item = items.NeiHanItem()
            item['username'] = username
            item['createtime'] = create_time
            item['content'] = content

            yield item






