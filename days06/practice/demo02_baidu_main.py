# -*- coding:utf-8 -*-

#引入测试模块
from selenium import webdriver

#启动phantonjs无界面浏览器
driver = webdriver.PhantomJS()

#访问百度首页
driver.get("http://www.baidu.com")

#查看访问百度首页的截图
# driver.save_screenshot("biadu1.png")

#获取百度的搜索输入框
keyword = driver.find_element_by_id("kw")
#向输入框中输入一个需要搜索的关键字
keyword.send_keys("huochepiao")

#重新查看截图，得到新的搜索页面的数据
driver.save_screenshot("baidu2.png")

#开始搜索：点击百度页面的搜索按钮，对输入的关键字进行搜索
btn = driver.find_element_by_id('su').click()

#查看搜索页面的结果
import time
time.sleep(1)
driver.save_screenshot("baidu3.png")

