# -*- coding:utf-8 -*-
"""
通过csdn账号密码登录，完成post请求的处理过程
"""

#引入scrapy模块
import scrapy

class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["csdn.net"]
    start_urls = ["https://passport.csdn.net/account/login?ref=toolbar"]

    def parse(self,response):
        #得到请求中需要的登录流水号--->在提交表单中的类型为hidden的input框--反爬操作
        lt = response.xpath("//input[@name='lt']/@value").extract()[0]
        #通过响应的对象，构建一个post请求发送

        return scrapy.FormRequest.from_response(
            response,
            # 根据需要爬取页面的数据进行构造数据
            formdata={
                "username":"15682808270",
                "password":"DAMUpython2016",
                "lt":lt
            },
            callback=self.parse_response
        )

    def parse_response(self,response):
        """
        处理post请求响应的数据
        :param response:
        :return:
        """
        with open("csdn.html" ,'w') as f:
            f.write(response.body)
