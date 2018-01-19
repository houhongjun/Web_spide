# -*- coding:utf-8 -*-

#引入需要的scrapy模块
import scrapy
#导入上一级的items模块
from .. import items
class ZhiLianSpider(scrapy.Spider):
    """
    智联招聘数据采集爬虫程序
    """
    #定义爬虫的名称，用于在命令中调用
    name = "zlspider"
    #定义域名限制：只能爬取--zhaopin.com域名下的所有数据
    allowed_domains = ["zhaopin.com"]

    #定义初始url地址--建议使用元组
    start_urls = (
        "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2b%E4%B8%8A%E6%B5%B7%2b%E5%B9%BF%E5%B7%9E%2b%E6%B7%B1%E5%9C%B3&kw=python&isadv=0&sg=7cd76e75888443e6b906df8f5cf121c1&p=1",
        # "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=1",
        # "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=2",
        # "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=3",
        # "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=4",
        # "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=5",
        # "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=6",
        # "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=7",
        # "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E7%88%AC%E8%99%AB&sm=0&sg=cab76822e6044ff4b4b1a907661851f9&p=8",
    )

    def parse(self,response):
        """
        采集到数据之后，自动执行的函数，主要进行如下功能
            筛选数据->封装Item对象->传递数据给Pipelines
            # >>>模拟--保存数据到文件
        :param response:
        :return:
        """
        # print(response.body)

        # filename = response.url.split("&")[-1] + ".html"
        # with open(filename,"w") as f:
        #     #爬虫程序采集到的数据，会封装在response.body属性中，可以直接获取
        #     f.write(response.body)

        # job_itmes = []

        job_list = response.xpath("//div[@id='newlist_list_content_table']/table[position()>1]/tr[1]")

        #提取所有的工作信息列表selector列表
        for select in job_list:
            job = select.xpath("td[@class='zwmc']/div/a/text()").extract()[0]
            #//div[@id='newlist_list_content_table']/table[@class='newlist']//tr[1]/td[@class='gsmc']
            company = select.xpath("td[@class='gsmc']//a/text()").extract()[0]
            salary = select.xpath("td[@class='zwyx']/text()").extract()[0]

            #封装成item 对象
            item = items.ZhiLianItem()
            item["job"] = job
            item["company"] = company
            item["salary"] = salary

            #将本次生成的item对象交给pipeline进行处理
            yield item

        #再次从响应中获取要进行下一次爬取的url地址[其他页面请求]
        next_page = response.xpath("//div[@class='pagesDown']/ul/li/a/@href").extract()

        #循环处理请求
        for page in next_page:

            page = response.urljoin(page)
            #重新发起请求采集下一组url地址的数据：[第一个参数：发起请求的url地址，第二个参数：请求数据一旦被采集--交给那个函数进行处理]

            yield scrapy.Request(page,callback=self.parse)

            # job_itmes.append(item)
        # return job_itmes




    # response.xpath("")提取需要的数据
    #
    # from items import ZhilianItem
    # item = ZhilianItem()
    # 保存需要的数据[job、company、salary]
    #
