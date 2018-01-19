# -*- coding:utf-8 -*-
#  贴吧爬虫案例
import urllib
import urllib2


def loadPage(url, filename):
    print filename + '正在下载'
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    }
    request = urllib2.Request(url, headers=header)
    return urllib2.urlopen(request).read()


def writePage(html,filename,page,kw):
    print filename + '正在保存'
    with open(r'F:\tieba\%s_%s.html' % (kw, page), 'w') as f:
        f.write(html)


def tiebaSpider(url, beginPage, endPage, kw):
    # 拼接各页链接
    print type(endPage)
    for page in range(int(beginPage), int(endPage)+1):
        pn = (page - 1) * 50
        filename = '第' + str(page) + '页.html'
        fullurl = url + '&pn=' + str(pn)
        html = loadPage(fullurl, filename)
        writePage(html, filename, kw, page)
    print '网页获取成功，感谢使用'


if __name__ == '__main__':
    kw = raw_input('请输入需要爬取的贴吧名：')
    beginPage = raw_input('请输入起始页：')
    endPage = raw_input('请输入结束页：')

    url = 'http://tieba.baidu.com/f?'
    key = urllib.urlencode({'kw':kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage, kw)
