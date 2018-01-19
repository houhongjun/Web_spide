# -*- coding:utf-8 -*-

#引入需要的模块
import urllib2
#引入该模块，用于进行编码
import urllib
#导入时间模块
import datetime
#导入原生的时间模块
import time


#定义爬取的网站路径
def engine(url,beginPage,endPage,kw,time_start):
    #拼接各个页面的连接
    print type(endPage)
    time1 = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    #爬取页面时，设置需要爬取的页面
    for page in range(int(beginPage),int(endPage)+1):
        pn = (page-1)*50
        filename = '第' + str(page) + '页.html'
        fullurl = url + '&pn='+str(pn)
        content = load_page(fullurl,filename)
        write_data(content,filename,kw,page)
    print '网页获取成功，感谢使用!保存时间：%s' % time1

    time_end = time.time()
    time_use = time_end-time_start
    print "爬取网页用时：%s秒"%time_use


#开始爬取网页页面
def load_page(url,filename):
    print filename + "正在下载"


    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",

    }
    request = urllib2.Request(url,headers=header)
    return urllib2.urlopen(request).read()

def write_data(content,filename,kw,page):
    print filename + "正在保存"


    #先用utf-8进行解码，然后使用gbk进行编码成中文的格式
    kw = kw.decode('utf-8').encode('gbk')
    with open(r'%s_%s.html' %(page,kw),'w') as f:
        f.write(content)
        print len(content)/1024


if __name__ == "__main__":
    kw = raw_input("请输入需要爬取的贴吧名称：")
    beginPage = raw_input("请输入需要爬取起始页：")

    endPage = raw_input("请输入需要爬取结束页：")
    time_start = time.time()
    url = 'https://tieba.baidu.com/f?'
    key = urllib.urlencode({'kw':kw})
    fullurl = url + key

    engine(fullurl,beginPage,endPage,kw,time_start)