# -*- coding:utf-8 -*-
"""
    爬取豆瓣电影模块下的 电影名称和评分
    js url: https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0
"""

# 引入需要的模块
import urllib2
import urllib
import random
import re
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 定义可爬取的模块列表
movie_type = ["热门", "最新", "经典","可播放", "豆瓣高分", "冷门佳作", "华语", "欧美", "韩国", "日本", "动作", "喜剧", "爱情", "科幻", "悬疑", "恐怖", "冷门"]

# 获取要爬取的模块
print("可选爬取的模块有:热门、最新、经典、可播放、豆瓣高分、冷门佳作、华语、欧美、\n韩国、日本、动作、喜剧、爱情、科幻、悬疑、恐怖、冷门")
tag = raw_input("请输入您要爬取的模块:")
if tag in movie_type:

    # 获取要爬取的页数
    page_limit = raw_input("请输入您要爬取的影片数量：")

    # 定义访问的url
    url = "https://movie.douban.com/j/search_subjects?"

    # 定义请求内容
    formdata = {
        "type": "movie",
        "tag": tag,
        "sort": "recommend",
        "page_limit": page_limit,
        "page_start": 0,
    }
    formda = urllib.urlencode(formdata)

    # 定义伪装请求ua
    ua = [
        "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
        ":Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,keGecko)Version/5.1Safari/534.50",
        "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
        "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
        "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
        "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)",
    ]
    # 随机获取一个User-agent身份标识
    user_agent = random.choice(ua)

    # 完整的请求路径
    full_url = url + formda

    # 定义请求对象
    print("开始抓取数据...")
    request = urllib2.Request(full_url)
    request.add_header("User-gent", user_agent)

    # 发送并获取数据
    response = urllib2.urlopen(request)
    content = response.read()

    # 对抓取的数据进行筛选
    print("数据抓取完成，正在对抓取到的数据进行筛选...")
    # 将content转化为json对象
    content_json = json.loads(content)
    # 获取电影列表
    movie_list = content_json["subjects"]
    # 循环得到title和rate的别表
    movies = ""
    for item in movie_list:
        title = item["title"]
        rate = item["rate"]
        movie_info = "电影名：%s,评分：%s;\n" % (title, rate)
        movies = movies + movie_info
    print("开始保存文件...")
    fime_name = tag.decode("utf-8").encode("gbk")

    # 保存数据
    with open(r"E:\Web_spide\movices\\" + fime_name + "_movies.txt", "w") as f:
        f.write(movies)
    print("文件保存成功")
else:
    print("没有相关模块")