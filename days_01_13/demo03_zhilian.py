# -*- coding:utf-8 -*-



#//table[@class='newlist'][20]/tbody/tr[1]
#引入需要的模块
import requests
from lxml import etree
import re
import bs4
import time
import datetime
import os

#设置count用于计数
count = 0

#需要爬取的页数
page = int(raw_input("请输入需要爬取的页数："))
#需要爬取的内容
job_want = raw_input("请输入需要爬取的工作：")
#需要爬取的城市
job_city = raw_input("请输入需要爬取的城市(多个城市用';'分隔)：")

#设置请求头
headers = {
    "User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",

}
page_count = 1
while page_count <= page:
    page_count += 1
    #设置请求路径
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?"

    #设置传递参数，get方式进行传递参数
    get_data = {
        "jl":job_city,
        "kw":job_want,
        "p":page,
        "isadv":0,
    }

    #发送请求并获取数据
    response = requests.get(url,headers=headers,params=get_data)
    content = response.text

    #通过path路径匹配目标数据
    content_xpath = etree.HTML(content)
    print(content_xpath)


    #得到数据的条数
    job_names = content_xpath.xpath("//tr[1]/td[@class='zwmc']/div/a[1]")
    job_num = len(job_names)
    print (job_num)


    #爬取的信息编号
    msg_num = 2
    for i in range(0,job_num):
        #通过xpath匹配具体数据

        #得到公司的相关信息
        company_info = content_xpath.xpath("//div[@id='newlist_list_content_table']/table[@class='newlist'][%s]//tr[1]" % msg_num)
        company_info = company_info[0].xpath("string(.)")
    #     #得到职位名称
    #     job_name = content_xpath.xpath("//table[@class='newlist'][%s]//tr[1]/td[@class='zwmc']/div/a[1]" % msg_num)
    #     job_name = job_name[0].xpath("string(.)")
    #
    #     #得到该公司的名称 # //table[@class='newlist'][%s]//tr[1]/td[@class='zwmc']/div/a[1]
    #     job_company = content_xpath.xpath("//table[@class='newlist'][%s]//tr[1]/td[@class='gsmc']/a[1]" % msg_num)

    #     job_company = job_company[0].xpath("string(.)")
    #
    #     #得到职位月薪
    #     job_pay = content_xpath.xpath("//table[@class='newlist'][%s]//tr[1]/td[@class='zwyx']" % msg_num)
    #     job_pay = job_pay[0].xpath("string(.)")
    #
    #     # 得到工作地点
    #     job_place = content_xpath.xpath("//table[@class='newlist'][%s]//tr[1]/td[@class='gzdd']" % msg_num)
    #     job_place = job_place[0].xpath("string(.)")
    #
        msg_num += 1
        count += 1
        # 拼接完整的一条职位信息
        full_msg = u"%s.相关信息：%s;\n" % (count,company_info)
        print(full_msg)
    #     # 将信息写入文件中
    #     with open("zhaopin/zhilian.txt", "a") as f:
    #         f.write(full_msg.encode("utf-8"))
    # log_time = str(datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"))
    #
    # log_msg = "爬虫程序在%s，向zhilian.txt文件中存入了%s条数据\n" % (log_time, count)
    # with open("zhaopin/log.txt", "a") as f:
    #     f.write(log_msg)





















































