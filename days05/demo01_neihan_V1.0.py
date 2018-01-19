# -*- coding:utf-8 -*-
############
#在正则匹配的时候一定要注意匹配的规则
############

#引入需要的模块
import requests
import re

#定义请求地址
url = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1515747172.8100002"

#定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    "X-CSRFToken": "53bc255c31855e0f7b0e6d51e852dfbd",
    "Referer": "http://neihanshequ.com/"
}

num =0
while num < 5:
    # 1.爬取目标数据
    #向指定url发送请求，获取数据
    response1 = requests.get(url,headers=headers)
    #打印展示
    content = response1.text
    print (content)

    #2.正则表达式筛选目标数据---一定要注意正则表达式的书写
    joke_list = re.findall(r'"content": "(.*?)",',content)
    print(joke_list)

    #3.存储数据[存储到文件|数据库]
    f = open("joke2.txt","a")
    for joke in joke_list:
        print(joke.decode("unicode-escape"))
        f.write(joke.decode("unicode-escape").encode("utf-8"))
        f.write("\r\n###################################################\r\n")

    f.close()


    num += 1


