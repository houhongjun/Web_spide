# -*- coding:utf-8 -*-

#引入需要的模块
import urllib2
import urllib
import random

import re

#定义伪装请求的ua
ua = [
    "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
    "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
]

#随机获取一个ua作为身份标识
user_agent = random.choice(ua)

#定义传送的数据
keyword = raw_input("请输入需要查找图片的关键字：")
startnum = raw_input("请输入需要图片的开始编码：")
photonum = raw_input("请输入需要图片数量：")
get_param = {
    "word":keyword,
    "pn":startnum,
    "rn":photonum,
}

#重新编码
data = urllib.urlencode(get_param)

#定义url地址
#word=%E5%BE%AE%E8%B7%9D%E6%91%84%E5%BD%B1&pn=0&rn=10
url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&"
full_url = url +data

print (full_url)

#请求封装对象
request = urllib2.Request(full_url,headers={"User-agent":user_agent})
# request.add_header("User-agent",user_agent)

#发送请求得到相应的数据
response = urllib2.urlopen(request)

result = response.read()
img_list = []
img_list = re.findall('"thumbURL":"(.*?)"', result)
#查看得到的图片地址列表
print img_list
img_re_list = []
#判断得到列表中的url地址是否为空值，筛出空值
for img_url in img_list:
    if img_url:
        img_re_list.append(img_url)


for i in range(0,len(img_re_list)):
    img_url = img_re_list[i]
    img_request = urllib2.Request(img_url)
    request.add_header("User-agent", user_agent)

    # 发送请求得到相应的数据
    img_response = urllib2.urlopen(img_request)

    img_result = img_response.read()
    filename = "img_"+str(i)+"_"+".jpg"
    with open(r"E:\Web_spide\sphoto\\"+filename,'wb') as f:
        f.write(img_result)


# print (result)
# print type(result)





