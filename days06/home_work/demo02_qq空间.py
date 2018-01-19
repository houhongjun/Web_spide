# -*- coding:utf-8 -*-
"""
使用selenium和phantomjs登录qq空间
"""

#引入需要的模块
from selenium import webdriver
import time

#启动phantomjs无界面浏览器
driver = webdriver.PhantomJS()
#打开qq空间登录界面
driver.get("https://qzone.qq.com/")
driver.maximize_window()

#查看是否成功获取qq空间登录界面
# driver.save_screenshot("qq1.png")

#form表单提交

#切换到登录框架
driver.switch_to.frame("login_frame")

driver.find_element_by_id("switcher_plogin").click()

#截图--查看是否成功获取到登录界面
# driver.save_screenshot("qq2.png")

#使用qq账号密码登录，获取输入账号框
driver.find_element_by_id("u").send_keys(u"318866913")
time.sleep(1)

driver.find_element_by_id("p").send_keys(u'hhj3188669913')
time.sleep(1)

#截图，检查账号密码登录是否成功
driver.save_screenshot("qq3.png")

#获取登录按钮，登录
driver.find_element_by_id("login_button").click()

time.sleep(3)
#截图，检查登录是否成功
driver.save_screenshot("qq4.png")


