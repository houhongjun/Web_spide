# -*- coding:utf-8 -*-

#引入scrapy模块
import scrapy

class GetSpider(scrapy.Spider):
    name = "getspider"
    allow_domains = ['baidu.com']
    start_urls = [
        'http://www.baidu.com'
    ]

    def parse(self,response):
        #进行响应数据的处理
        """
        起始请求的数据采集工作，由scrapy框架自动完成
            爬虫[起始地址列表start_urls]
                -->scrapy.Spider -->Request()请求对象
                    -->scrapy.engine 引擎对象
                        -->scrapy.schedual 调度模块
                            -->scrapy.download 下载模块
                                -->scrapy.engine 引擎模块
                -->自写爬虫程序[得到数据]
        -->爬虫[parse()函数进行后续的数据处理]
        请求的操作--不能由爬虫程序控制，而是scrapy自动调度，发送get请求
        :param response:
        :return:
        """
        pass


class PostSpider(scrapy.Spider):

    """
    post请求操作爬虫
    """
    name = "postspider"
    allowed_domains = ['renren.com']
    start_urls = [
        "http://www.renren.com/login"
    ]

    def start_requests(self):
        """
        重写start_request()函数，发送自定义请求
        :return:
        """
        # return scrapy.Request(self.start_urls[0],method='POST')
        return scrapy.FormRequest(
            self.start_urls[0],
            formdata={
                "username":"admin",
                "password":"123",
            },
            callback=self.parse_response
        )
    def parse_response(self,response):
        """
        这个函数中，专门用来处理post请求得到的响应数据
        :param response:
        :return:
        """
        pass
    
