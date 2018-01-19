# -*- coding:utf-8 -*-

#引入scrapy模块
import scrapy

from ..items import ZhilianItem

class ZhilianSpider(scrapy.Spider):
    """
    智联招聘数据采集爬虫程序
        需要继承scrapy.Spider类型，让scrapy负责调度爬虫程序进行数据的采集
    """
    #name属性：爬虫名称
    name = "zlzp"
    #allwoed_domains属性：限定采集数据的域名
    allwoed_domains = ['zhaopin.com']
    #起始url地址
    start_urls = [
        'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2b%E4%B8%8A%E6%B5%B7%2b%E5%B9%BF%E5%B7%9E%2b%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=7cd76e75888443e6b906df8f5cf121c1&p=1',
    ]

    def parse(self,response):
        """
        采集的数据解析函数(响应数据解析函数)
            主要用于进行响应数据的筛选：筛选目标数据封装成Item对象
        :param response:
        :return:
        """

        url = response.urljoin(self.start_urls[0])
        yield scrapy.Request(url,callback=self.parse_response)

    def parse_response(self,response):
        #筛选得到工作列表
        job_list = response.xpath("//div[@id='newlist_list_content_table']/table[position()>1]/tr[1]")

        #循环获取采集的字段信息
        for job in job_list:
            #岗位名称
            job_name = job.xpath("td[@class='zwmc']/div/a").xpath("string(.)").extract()[0]
            #公司名称
            company = job.xpath("td[@class='gsmc']/a").xpath("string(.)").extract()[0]
            #薪水
            salary = job.xpath("td[@class='zwyx']").xpath("string(.)").extract()[0]

            # 封装成item对象
            item = ZhilianItem()
            item['job_name'] = job_name
            item['company'] = company
            item['salary'] = salary

            #通过协程的方式移交给pipeline进行处理
            yield item

        #再次从响应中获取要进行下一步爬取的url地址[其他页面请求]
        next_page = response.xpath("//div[@class='pagesDown']/ul/li/a/@href").extract()
        #循环处理请求
        for page in next_page:
            page = response.urljoin(page)
            #重新发起请求采集下一组url地址的数据[第一个参数：发起的请求地址，第二个参数：请求数据一旦被采集--交给那个函数进行处理]
            yield scrapy.Request(page,callback=self.parse_response)

