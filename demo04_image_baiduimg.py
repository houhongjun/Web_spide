# -*- coding:utf-8 -*-
"""
    爬取百度图片：战舰世界相关
    url:
    http://image.baidu.com/search/index?
    tn=baiduimage&ipn=r&ct=201326592&cl=2
    &lm=-1&st=-1&fm=index&fr=&hs=0
    &xthttps=000000&sf=1&fmq=&pv=&ic=0&nc=1&z=
    &se=1&showtab=0&fb=0&width=&height=&face=0&istype=2
    &ie=utf-8&word=%E6%88%98%E8%88%B0%E4%B8%96%E7%95%8C&oq=
    %E6%88%98%E8%88%B0%E4%B8%96%E7%95%8C&rsp=-1
"""
# 引入需要的模块
import urllib2
import re
import urllib
import random

# 设置请求头
headers = {
    "GET http": "//image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%88%98%E8%88%B0%E4"
                "%B8%96%E7%95%8C&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%88%98%E8%88%B0%E4%B8%96%E7%95%8C&s"
                "=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=60&rn=30&gsm=3c&1515482751935= HTTP/1.1",
    "Host": "image.baidu.com",
    "Connection": "keep-alive",
    "Accept": "text/plain, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Referer": "http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq"
               "=1515482370103_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%88%98%E8%88%B0%E4%B8%96%E7%95%8C",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "BDIMGISLOGIN=0; winWH=%5E6_1366x623; "
              "BDqhfp=%E6%88%98%E8%88%B0%E4%B8%96%E7%95%8C%26%260-10-1undefined%26%260%26%261; __cfduid=d85ef628c3d5b2955cdfb667914920a4b1506413584; BAIDUID=BC3E671A480178117F7F9130BB5F2087:FG=1; BIDUPSID=BC3E671A480178117F7F9130BB5F2087; PSTM=1515223551; BDUSS=U1SH55NlFyWExqdHJKa1hFaFVFVm9sZW9Zc2ZHdnBETVJQdU1vMUl0Q3czM3BhQVFBQUFBJCQAAAAAAAAAAAEAAAAZuDCHweNXWUY5NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALBSU1qwUlNaQl; locale=zh; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=5; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1446_13550_21083_20927; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1; BCLID=12820342338954146579; BDSFRCVID=AR-sJeC62meI7U6AoMSjb7qVBN2ksNRTH6bHuDsN1xQjOWefFvDCEG0Pqx8g0Ku-hEJYogKKBeOTHn3P; H_BDCLCKID_SF=tJPHoC-htI03qnRTqRQaq4tehHRCtJQeWDTm_D_2LfccJK5qhUc65-jWKJjG2t7vQIjB-pPKKqnJKJnNyTu-5tcQbtc4K5Jn3mkjbPjyfn02OP5PMKcjj-4syPRGKxRnWI_ebIF5tK0KbKLmen8_M-A-qxby26nCLtjeaJ5nJDoVeqI63jjNhUu9MxKfbl5GBJrWQhr4QpP-HlnGQbbFDJkuM4nUK45lbenmKl0MLPjWbb0xyn_VMMLpWfnMBMnG5mOnanubLIcjqR8ZD6-Wj6bP; indexPageSugList=%5B%22%E6%88%98%E8%88%B0%E4%B8%96%E7%95%8C%22%2C%22%E6%B2%99%E6%BC%A0%E4%B9%8B%E9%B9%B0%E6%89%8B%E6%9E%AA.50%22%2C%22%E6%B2%99%E6%BC%A0%E4%B9%8B%E6%89%8B%E6%9E%AA%22%2C%22%E6%B2%99%E6%BC%A0%E4%B9%8B%E9%B9%B0%22%2C%22%E5%8A%A0%E7%89%B9%E6%9E%97%E6%9C%BA%E6%9E%AA%22%2C%22%E6%88%98%E8%88%B0%E4%B8%96%E7%95%8C%E9%9E%8D%E5%B1%B1%E5%A3%81%E7%BA%B8%22%2C%22%E6%88%98%E8%88%B0%E4%B8%96%E7%95%8C%E8%83%A1%E5%A4%A7%E5%92%8C%E7%BA%B8%22%2C%22%E6%88%98%E8%88%B0%E4%B8%96%E7%95%8C%E8%83%A1%E5%BE%B7%E5%A3%81%E7%BA%B8%22%2C%22%E6%88%98%E8%88%B0%E4%B8%96%E7%95%8C%E5%AF%86%E8%8B%8F%E9%87%8C%22%5D; cleanHistoryStatus=0; userFrom=www.baidu.com",

}

# 定义伪装请求的ua
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
# 随机获取url标识
user_agent = random.choice(ua)

# 定义url地址
url = "http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%88%98%E8%88%B0%E4%B8%96%E7%95%8C&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%88%98%E8%88%B0%E4%B8%96%E7%95%8C&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=60&rn=30&gsm=3c&1515482751935="

# 发送请求并获取数据
response = urllib2.urlopen(url)
content = response.read()
urls = re.findall('"hoverURL":"(.*?)"', content)

# 循环获取图片路径并爬取图片
for i in range(0, len(urls)):
    img_url = urls[i]
    print(img_url)
    # 封装请求对象
    request_image = urllib2.Request(img_url,headers=headers)
    request_image.add_header("User-agent", user_agent)
    # 发送并获取图片数据
    response_image = urllib2.urlopen(request_image)
    image = response_image.read()
    image_name = "image" + "_" + str(i) + ".jpg"
    print(image)
    # 保存图片
    with open("images/"+image_name, "wb") as f:
        f.write(image)
