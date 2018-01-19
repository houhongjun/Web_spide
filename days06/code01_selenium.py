# -*- coding:utf-8 -*-

from selenium import webdriver

# driver = webdriver.Chrome()
driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com")
print(driver.title)
#1.保存访问的截图
driver.save_screenshot('baidu1.png')
#2.保存访问的数据的源代码
with open("baidu.html",'w') as f:
    f.write(driver.page_source.encode('utf-8'))
# driver.quit()



