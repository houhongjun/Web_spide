#  -*- coding:utf-8 -*-
"""
基于scrapy.spiders.CrawlSpider的深度爬虫操作
"""

#引入需要的模块
#引入CrawlSpider爬虫模块和Rule操作规则模块
from scrapy.spider import CrawlSpider,Rule
#引入连接模块 LinkExtractor
from scrapy.linkextractors import LinkExtractor


class ZhilianSpider(CrawlSpider):
    """
    基于CrawlSpider的爬虫程序
    """
    #定义属性
    name = 'zl'
    #定义域名限制
    allowed_domains = ["zhaopin.com"]

    #定义其实url地址
    start_urls = ["http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2b%E4%B8%8A%E6%B5%B7%2b%E5%B9%BF%E5%B7%9E%2b%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=7cd76e75888443e6b906df8f5cf121c1&p=1",]
    #定义链接提取规则
    link_extractor = LinkExtractor(
        allow=(r"888443e6b906df8f5cf121c1&p=\d+")
    )

    #定义链接操作规则
    rules = [
        Rule(link_extractor,follow=True,callback="parse_response"),
    ]

    #注意：不能重写parse()函数：因为在父类中已经重写过了parse()函数
    #如果我们再次重写该函数··-深度采集数据就会失效

    def parse_response(self,response):
        #处理响应数据
        #提取当前页的所有工作列表
        job_list = response.xpath("//div[@id='newlist_list_content_table']/table[position()>1]/tr[1]")
        #处理每个工作信息
        for job in job_list:
            job_name = job.xpath("td[@class='zwmc']/div/a").xpath("string(.)").extract()[0]
            print(job_name)

        print ("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*")
