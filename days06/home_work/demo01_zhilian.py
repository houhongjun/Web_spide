# -*- coding:utf-8 -*-

#引入自动化测试
from selenium import webdriver

#启动phantomjs无界面浏览器
driver = webdriver.PhantomJS()

#1.访问智联招聘首页面
driver.get("http://ts.zhaopin.com/jump/index.html?sid=121127632&site=yi_dqty_000020")

#截图查看是否访问成功
# driver.save_screenshot("zlzp1.png")

#2.登录表单中填写数据
btn1 = driver.find_element_by_css_selector(".tab_0517 .li2 current").click()

# driver.find_element_by_id("loginname").send_keys(u"15237368921")
# driver.find_element_by_id("password").send_keys(u'hhjlovecnn1314')

#截图查看数据是否正常
driver.save_screenshot("zlzp2.png")
