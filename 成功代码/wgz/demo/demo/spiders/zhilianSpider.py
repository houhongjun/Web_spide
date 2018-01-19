# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/16 11:44'

# 引入需要的模块
import scrapy
from .. import items

class zhilianSpider(scrapy.Spider):
    '''
    智联招聘数据采集爬虫程序
    '''
    # 定义爬虫名称，用于命令中调用
    name = 'zlspider'
    # 定义域名限制：只能爬取域名下的数据
    allowed_domains = ['zhaopin.com']
    # 定义初始url地址
    start_urls = (
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=1",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=2",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=3",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=4",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=5",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=6",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=7",
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=8",
    )

    def parse(self, response):
        '''
        采集到数据之后，自动执行的函数，主要进行如下功能：
        数据筛选->封装Item对象->传递数据给piperlines >>> 模拟保存数据到文件
        :param response:
        :return:
        '''
        # filename = response.url.split('&')[-1] + '.html'
        # with open(filename, 'w') as f:
        #     # 爬虫采集到的数据，会封装在response.body属性中，可以直接获取
        #     f.write(response.body)
        '''
        response.xpath('')提取需要的数据
        item = zhilianItem()
        保存需要的数据[job, company, money]
        '''

        job_list = response.xpath("//div[@id='newlist_list_content_table']/table[@class='newlist']/tr[1]")
        for it in job_list:
            print '********'
            job = it.xpath("td[@class='zwmc']/div/a/text()").extract_first()
            company = it.xpath("td[@class='gsmc']/a[1]/text()").extract_first()
            money = it.xpath("td[@class='zwyx']/text()").extract_first()
            # print(job)
            # print(company)
            # print(money)
            item = items.zhilianItem()
            item['job'] = job
            item['company'] = company
            item['money'] = money

            # 将本次生成的item对象交给pipeline进行处理
            yield item

