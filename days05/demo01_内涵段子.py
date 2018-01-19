# coding:utf-8

#引入需要的模块
import requests
import re

#定义请求地址
url = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1515714453"

# 定义请求头
headers = {
    "Referer":"http://neihanshequ.com/",
    "X-CSRFToken":"6696c65bb67a313dd2fd928120876648",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.7 Safari/537.36"
}
num = 0
while num < 5:
    #######################1. 爬取目标数据
    # 向指定url发送请求，获取数据
    response1 = requests.get(url, headers=headers)
    # 打印展示
    content = response1.text
    #print(response1.text)

    #######################2. 正则表达式筛选目标数据
    joke_list = re.findall(r'"content": "(.*?)"', content)
    print(joke_list)

    #######################3. 存储数据[存储到文件|数据库]
    f = open("joke1.txt", "a")

    for joke in joke_list:
        print(joke.decode("unicode-escape"))
        f.write(joke.decode("unicode-escape").encode("utf-8"))
        f.write("\r\n###################################################\r\n")

    f.close()

    num += 1


# [重点]请求url地址的分析
# [重点]请求到的数据[正则匹配 + 数据转换[编码]]
