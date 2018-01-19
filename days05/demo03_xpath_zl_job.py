# -*- coding:utf-8 -*-

import requests
from lxml import etree

url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E4%B8%8A%E6%B5%B7%2B%E5%B9%BF%E5%B7%9E%2B%E6%B7%B1%E5%9C%B3&kw=python&p=1&isadv=0 "
headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    "Referer": "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC%2B%E4%B8%8A%E6%B5%B7%2B%E5%B9%BF%E5%B7%9E%2B%E6%B7%B1%E5%9C%B3&kw=python&sm=0&p=1",
}

#发送请求，获取智联网页数据
response = requests.get(url,headers=headers)
html_str = response.text

#xpath  匹配目标数据
html = etree.HTML(html_str)
print(html)#<Element html at 0x5b11908>

#1.xpath匹配数据：注意：原始THML数据和网页中能看到的数据--不一定是一致的，一定要对xpath进行测试，确定符合自己要求

job_names = html.xpath("//div[@id='newlist_list_content_table']/table[@class='newlist']/tr[1]/td[@class='zwmc']/div")

print(job_names)
f = open("zljob.txt","w")
for job_name in job_names:
    f.write(job_name.xpath("string(.)").strip().encode("utf-8")+"\r\n")

f.close()
