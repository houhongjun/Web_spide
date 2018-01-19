# -*- coding:utf-8 -*-

# 引入需要的模块
from selenium import webdriver
#打开phantom js 无界面浏览器
#如果phantomjs浏览器可执行文件已经配置到系统环境变量中，
#直接通过下面的代码启动浏览器即可
driver = webdriver.PhantomJS()


# 如果没有配置环境变量，需要指定路径启动phantomjs，如下：
# driver = webdriver.PhantomJS("./phantomjs-2.1.1-windows/bin/phantomjs")
#模拟浏览器地址栏输入并访问http://www.baidu.com
driver.get("http://www.baidu.com")

#查看访问结果：
#1.保存访问的截图
driver.save_screenshot("baidu1.png")

#2.保存访问的数据源代码
with open("baidu.html",'w') as f:
    f.write(driver.page_source.encode('utf-8'))

