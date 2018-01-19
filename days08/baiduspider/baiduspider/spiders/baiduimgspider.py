# -*- coding:utf-8 -*-

#引入需要的模块
import scrapy
#导入上级的items模块

class BaiDuSpider(scrapy.Spider):
    """
    百度图片数据采集爬虫程序
    """
    #定义爬虫名称，用于在命令中调用
    name = 'bdspider'
    #定义域名限制：只能爬取--image.baidu.com域名下的所有数据
    allowed_domains = ['image.baidu.com']

    #定义初始url地址---建议使用元组
    start_urls = ("https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord=%E5%A3%81%E7%BA%B8&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E5%A3%81%E7%BA%B8&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&cg=wallpaper&pn=300&rn=30&gsm=12c&1516160492120=",)


    def parse(self,response):
        print('---*---*---*---*---*---*---*---*---*---*---*---*---*---*---*---')
        import re,time
        result = response.body
        print result
        # img_list = []
        #
        # img_list = re.findall('"thumbURL":"(.*?)"',result)
        # print ('--*--8--*--8--*--8--*--8--*--8')
        # print (img_list)
