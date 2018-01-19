# -*- coding:utf-8 -*-
# https://im.qq.com/

#引入测试模块
from selenium import webdriver
#引入时间模块
import time

#启动phantomjs无界面浏览器
driver = webdriver.PhantomJS()

#访问qq登录的页面
driver.get("https://im.qq.com/index.shtml")

#查看截图
driver.save_screenshot("qq1.png")

#点击qq主页的登录按钮，进行登录操作  forgetpwd
# btn = driver.find_element_by_id('login').click()
# driver.save_screenshot("qq2.png")


