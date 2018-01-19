#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'Mr.Xie'
__date__ = '2018.01.08 16:52'

import time
import os

import urllib2
from urllib import urlencode


def load_page(url, page):
    """用于下载文件"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}
    print("正在下载第{}页".format(page))
    req = urllib2.Request(url, headers=headers)
    web_data = urllib2.urlopen(req)
    return web_data.read()


def write_page(web_data, page, key):
    """用于保存文件"""
    print("正在保存第{0}-{1}页".format(key, page))
    with open("./web_data/{0}-{1}.html".format(key, page), 'w') as f:
        f.write(web_data)


def tieba_spider(key, end_page):
    """用于发送请求"""
    form_data = urlencode({"kw": key})
    part_url = 'http://tieba.baidu.com/f?{}'.format(form_data)
    for page in range(1, end_page):
        url = "{0}&pn={1}".format(part_url, (page - 1) * 50)
        web_data = load_page(url, page)
        write_page(web_data, page, key)


if __name__ == '__main__':
    """程序入口"""
    start = time.clock()  # 开始计时

    key = raw_input("请输入贴吧名称：")
    end_page = int(raw_input("请输入终止页码："))
    tieba_spider(key, end_page)

    elapsed = (time.clock() - start)  # 总共用时

    file_list = os.listdir("./web_data/")
    file_size = sum(map(lambda v: os.path.getsize('./web_data/' + v), [file for file in file_list])) / 1024 / 1024

    print("总计下载量:{0}M,总计用时:{1}s".format(file_size, elapsed))
