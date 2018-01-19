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
driver.save_screenshot("qq01.png")

#点击头像进行登录

driver.switch_to.frame("login_frame")
driver.find_element_by_id("img_out_610996675").click()
time.sleep(5)
# driver.find_element_by_id("img_out_610996675").click()
# time.sleep(5)

# html = driver.page_source
# print(html)
#
# #保存网页
# with open("qq_zone.html" ,'w') as f:
#     f.write(html.encode("utf-8"))
#
# #截图--检查qq空间登录是否成功
# driver.save_screenshot("qq5.png")

