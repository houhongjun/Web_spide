# -*- coding:utf-8 -*-
"""
    爬去特定的网页
    将不同功能的代码封装在不同的函数中进行操作
"""
# 引入需要的模块
import urllib2
import datetime


def engine():
    """爬虫引擎对象：专门用来调度所有的函数工作"""
    # 获取要爬取的贴吧名
    tieba = raw_input("输入要爬取的贴吧：")
    # 获取要爬去的起始页
    page_star = raw_input("请输入开始页:")
    # 获取要爬取的结束页
    page_end = raw_input("请输入结束页:")

    # 循环爬取目标贴吧
    for page in range(int(page_star), int(page_end)+1):
        # 当前爬取的页码
        page_now = (page - 1) * 50
        # 要爬去的网页地址
        url = "http://tieba.baidu.com/f?kw=" + tieba + "&ie=utf-8&pn=" + str(page_now)
        # 将爬取的数据保存在content变量中
        print("正在爬取%s吧的第%d页..." % (tieba, page))
        content = load_page(url)
        print("正在爬取%s吧的第%d页爬取完成，正在保存..." % (tieba, page))
        time = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
        tieba_code = tieba.decode("utf8").encode("gb2312")
        filename = tieba_code + "_" + str(page) + "_" + time + ".html"
        # 保存获取到的数据到对应的文件中
        write_data(filename, content)
        print("%s吧的第%d页保存完成。" % (tieba, page))
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("%s吧的爬取工作完成，程序结束！" % tieba)


def load_page(url):
    """爬取数据的函数"""
    # 爬去数据
    response = urllib2.urlopen(url)
    content = response.read()
    return content


def write_data(filename, content):
    """记录数据到文件的函数"""
    with open("download_file/" + filename, "w") as f:
        f.write(content)


if __name__ == '__main__':
    engine()
