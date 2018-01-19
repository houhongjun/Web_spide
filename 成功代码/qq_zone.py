# coding:utf-8
"""
    使用selenium和phantomjs登录qq空间
"""

# 引入需要的模块
from selenium import webdriver
import time

# 启动phantomjs无界面浏览器
# driver = webdriver.PhantomJS()
driver = webdriver.PhantomJS()
# 打开qq空间登录界面
driver.get("https://qzone.qq.com/")
driver.maximize_window()

# 截图
# driver.save_screenshot("qq1.png")

#####################form表单提交#####################################

# 切换到登录框架
driver.switch_to.frame("login_frame")

# driver.find_element_by_id("switcher_plogin").click()
#
# # 截图
# # driver.save_screenshot("qq2.png")
#
# # 获取输入框，并输入信息
# driver.find_element_by_id("u").send_keys(u"805587573")
# time.sleep(1)
# driver.find_element_by_id("p").send_keys(u"wang194591181wlf")
# time.sleep(1)
#
# #截图
# # driver.save_screenshot("qq3.png")
#
# # 获取登录按钮，登录
# driver.find_element_by_id("login_button").click()
#
# time.sleep(3)
#
# # 截图
# driver.save_screenshot("qq4-1.png")



###############点击头像登录#######################################

# 直接点击头像
driver.find_element_by_id("img_out_805587573").click()
time.sleep(5)

html = driver.page_source
print(html)

# 保存网页
with open("qq_zone.html", "w") as f:
    f.write(html.encode("utf-8"))

# 截图
driver.save_screenshot("qq5-1.png")
