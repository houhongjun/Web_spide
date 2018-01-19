# -*- coding:utf-8 -*-

# 引入需要的模块
import urllib2
import urllib
import random

import re

# 定义伪装请求的ua
ua = [
    "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
    "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
]

# 随机获取一个ua作为身份标识
user_agent = random.choice(ua)

# 定义传送的数据
keyword = raw_input("请输入需要查找图片的类型：")
page_limit = raw_input("需要查询的电影条数：")
# page_start = raw_input("请输入需要开始查询的位置：")
get_param = {
    "tag": keyword,
    "page_limit": page_limit,
    # "page_start":page_start,
}

# 重新编码
data = urllib.urlencode(get_param)

# 定义url地址
# word=%E5%BE%AE%E8%B7%9D%E6%91%84%E5%BD%B1&pn=0&rn=10
url = "https://movie.douban.com/j/search_subjects?type=movie&page_start=0&"
full_url = url + data

print (full_url)

# 请求封装对象
request = urllib2.Request(full_url, headers={"User-agent": user_agent})
# request.add_header("User-agent",user_agent)

# 发送请求得到相应的数据
response = urllib2.urlopen(request)

result = response.read()

img_list = []
img_list = re.findall('"cover":"(.*?)"', result)
# 查看得到的图片地址列表---封面图片的地址列表正确
# print img_list


for i in range(0, len(img_list)):
    img_url = img_list[i]
    print img_url
    request = urllib2.Request(img_url)
    print request

    # ----出现错误
    # < urllib2.Request
    # instance
    # at
    # 0x00000000052E4448 >
    # request.add_header("User-agent",user_agent)
    #
    # img_response = urllib2.urlopen(request)
    # img_result = img_response.read()
    # filename = "img_" + str(i)+"_"+".jpg"
    # with open(r"E:\Web_spide\days02_爬虫\doubaiP\\",'wb') as f:
    #     f.write(img_result)




    # request = urllib2.Request(img_url,headers={"User-agent":user_agent})

    # request.add_header("User-agent", user_agent)

    # 发送请求得到相应的数据
    # img_response = urllib2.urlopen(request)

    # img_result = img_response.read()
    # filename = "img_"+str(i)+"_"+".jpg"
    # with open(r"E:\Web_spide\sphoto\\"+filename,'wb') as f:
    #     f.write(img_result)


# print (result)
# print type(result)
