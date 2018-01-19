# -*- coding:utf-8 -*-
"""
爬取豆瓣电影模块下的 电影名称和评分
url :
https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0
并统计爬取文件的大小和所用时间
"""
#引入需要的模块
import requests
import random
import json
import datetime,time
import sys
import os

#记录本次爬虫程序启动的时间
spide_start = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
spide_start_log = str(datetime.datetime.now().strftime("%Y年%m月%d日：%H-%M-%S"))

#记录本次爬取的开始时间，用于计算程序用时
start_time = time.time()
# 定义可爬取的模块列表
movie_type = ["热门", "最新", "经典", "可播放", "豆瓣高分", "冷门佳作", "华语", "欧美", "韩国", "日本", "动作", "喜剧", "爱情", "科幻", "悬疑", "恐怖", "冷门"]

# 获取要爬取的模块
print("可选爬取的模块有:热门、最新、经典、可播放、豆瓣高分、冷门佳作、华语、欧美、\n韩国、日本、动作、喜剧、爱情、科幻、悬疑、恐怖、冷门")
tag = raw_input("请输入您要爬取的模块:")

#判断用户查询模块是否存在
if tag in movie_type:
    #获取需要爬取的页数:
    page_limit = raw_input("请输入需要爬取的影片数量：")

    #定义伪装请求ua
    ua = [
        "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
        "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
        "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
        "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)",
    ]
    #随机获取一个User-agent身份标识
    user_agent = random.choice(ua)
    #设置请求头
    headers = {
        "User-Agent":user_agent,
    }

    #设置传递的get参数
    get_data = {
        "tag":tag,
        "sort":"recommend",
        "page_limit":page_limit,
        "page_start":0,
    }
    #访问的url
    url = "https://movie.douban.com/j/search_subjects?type=movie&"
    #get方式发送请求，附带get_data参数
    response = requests.get(url,params=get_data,verify=False)

    #将获取得到的数据存储在content变量中
    content = response.text

    #将content 中的数据转化为json数据
    content_json = json.loads(content)

    #设置计数变量count
    count = 0

    #循环遍历所有的电影和评分以及url地址
    for item in content_json["subjects"]:
        title = item["title"]
        rate = item["rate"]
        url = item["url"]
        movie = u"电影名称：%s，评分：%s，url详情：%s\r\n" % (title,rate,url)
        print(movie)

        #设置保存的文件名
        file_name = tag.decode("utf-8").encode("gbk") + "_" + spide_start + ".txt"
        #保存电影信息到指定的文件夹中
        with open("douban/" + file_name , "a") as f:
            f.write(movie.encode("utf-8"))
            count += 1
    #记录本次爬取的结束时间，用于计算程序用时
    end_time = time.time()
    #计算本次爬取时间
    use_time = end_time - start_time
    #将时间保留两位小数
    use_time = round(use_time,2)

    #记录日志信息
    #获取文件大小
    file_path = "douban/" + file_name
    file_size = os.path.getsize(file_path)

    file_size = file_size / float(1024) #KB
    file_size = round(file_size,2)
    file_name_for_log = tag + "_" + spide_start +'.txt'

    log_msg = "爬虫程序在%s，保存了文件：%s，文件大小：%s KB，用时：%s 秒 \n" %(spide_start_log,file_name_for_log,file_size,use_time)

    #保存日志信息
    with open("douban/spider_log.txt","a") as f:
        f.write(log_msg)

else:
    print ("没有此模块")














































