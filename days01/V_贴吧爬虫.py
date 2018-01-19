# coding=utf-8
#  贴吧爬虫案例------可以实现统计文件的大小，同时将爬取的文件放在一个文件夹中
import urllib
import urllib2
import datetime,os

totalSize = 0
fileNum = 0
dirNum = 0
fileSize = ''


def loadPage(url, filename):
    print filename + '正在下载'
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    }
    request = urllib2.Request(url, headers=header)
    return urllib2.urlopen(request).read()



# E:\Web_spide\days01-----文件夹保存的路径，，保存在和代码相同的根目录之下。
def writePage(html,filename,kw,page):
    print filename + '正在完成保存'
    timenow = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    timenow = str(timenow)

    dirpath = 'E:\Web_spide\days01\\%s'%kw
    with open(r'%s\%s_%s_%s.html' % (dirpath,page, kw,timenow), 'w') as f:
        f.write(html)


def visitDir(path):
    global totalSize
    global fileNum
    global dirNum
    global fileSize
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        if os.path.isfile(sub_path):
            fileNum = fileNum+1
            totalSize = totalSize+os.path.getsize(sub_path)
            K, M, G = 1024, 1024 ** 2, 1024 ** 3
            if totalSize >= G:
                fileSize = str(totalSize / G) + 'G'
            elif totalSize >= M:
                fileSize = str(totalSize / M) + 'M'
            elif totalSize >= K:
                fileSize = str(totalSize / K) + 'K'
            else:
                fileSize = str(totalSize) + 'B'
        elif os.path.isdir(sub_path):
            dirNum = dirNum+1
            visitDir(sub_path)


def tiebaSpider(url, beginPage, endPage, kw):
    # 拼接各页链接
    kw = kw.decode('utf-8').encode('gb2312')
    os.mkdir('E:\Web_spide\days01\\%s' % kw)
    for page in range(int(beginPage), int(endPage)+1):
        pn = (page - 1) * 50
        filename = '第' + str(page) + '页.html'
        fullurl = url + '&pn=' + str(pn)
        html = loadPage(fullurl, filename)
        writePage(html, filename, kw, page)
    dirpath = 'E:\Web_spide\days01\\%s' % kw

    # 统计文件夹大小、数量
    if not os.path.isdir(dirpath):
        print('Error:"', dirpath, '" 未找到.')
        return
    visitDir(dirpath)
    os.rename(dirpath,'E:\Web_spide\days01\\%s_%sfiles_%s' % (kw,fileNum,fileSize))
    print '网页获取成功，感谢使用'


if __name__ == '__main__':
    kw = raw_input('请输入需要爬取的贴吧名：')
    beginPage = raw_input('请输入起始页：')
    endPage = raw_input('请输入结束页：')

    url = 'http://tieba.baidu.com/f?'
    key = urllib.urlencode({'kw':kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage, kw)
