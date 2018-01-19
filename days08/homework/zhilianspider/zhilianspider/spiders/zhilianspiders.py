# -*- coding:utf-8 -*-

#引入scrapy模块
import scrapy

from ..items import ZhiLianItem

class ZhilianSpider(scrapy.Spider):
    """
    智联招聘数据采集爬虫程序
        需要继承scrapy.Spider类型，让scrapy负责调度爬虫程序进行数据的采集
    """
    #name属性名称
    name = 'zhilian'
    #allowed_domains属性：限定采集数据的域名
    allowed_domains = ["zhaopin.com"]
    #起始url地址
    start_urls = ["http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%8A%E6%B5%B7&kw=python&sm=0&isfilter=0&fl=538&isadv=0&sg=da0238a52b6947d984dbc1d18e0a8dad&p=1"]

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
            #职务薪水
            salary = job.xpath("td[@class='zwyx']").xpath("string(.)").extract()[0]

            #封装成item对象
            item = ZhiLianItem()
            item['job_name'] = job_name
            item['company'] = company
            item['salary'] = salary

            #通过协程的方式移交给pipeline进行处理
            yield item

        #再次从响应中获取要进行下一次爬取的url地址[其他页面请求]
        next_page  = response.xpath("//div[@class='pagesDown']/ul/li/a/@href").extract()
        #循环处理
        for page in next_page:
            page = response.urljoin(page)
            #重新发起新的地址请求，采集下一组url地址的数据[第一个参数：发起请求的url地址，第二个参数：请求数据采集之后，对采集到的数据进行处理的函数名称]

            yield scrapy.Request(page,callback=self.parse_response)