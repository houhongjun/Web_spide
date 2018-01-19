# -*- coding:utf-8 -*-

#引入需要的模块
import urllib2
import urllib
import json

import sys
reload(sys)
sys.setdefaultencoding("utf8")

#定义访问的url
url = "https://movie.douban.com/j/search_subjects"
#定义请求头
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"
}

#定义可查询的类别名称
kinds = ["热门","最新","经典","可播放","豆瓣高分","冷门佳片","华语","欧美","韩国","日本","动作","喜剧","爱情","科幻","悬疑","恐怖","治愈"]
print '可供选择的影视类型：<热门>、<最新>、<经典>、\n' \
      '<可播放>、<豆瓣高分>、<冷门佳片>、<华语>、\n' \
      '<欧美>、<韩国>、<日本>、<动作>、<喜剧>、\n' \
      '<爱情>、<科幻>、<悬疑>、<恐怖>、<治愈>'

#输入需要查询类型的名称
kind = raw_input("请选择影视类型：")
if kind in kinds:

    nums = raw_input("请输入您需要获取电影数量：")

    fromdata = {
        "type":"movie",
        "tag":kind,
        "page_limit":nums,
        "page_start":'0',
    }
    #将输入的数据进行编码---encode
    data = urllib.urlencode(fromdata)
    # 创建url路径对象
    request = urllib2.Request(url,data=data,headers=headers)
    #返回对应的数据
    response = urllib2.urlopen(request).read()
    #根据返回数据的格式，将返回的数据定义为json格式
    moviejson = json.loads(response)
    movielist = moviejson['subjects']
    kind = (kind + '电影').decode('utf-8').encode('gbk')
    movies = ''
    for movie in movielist:
        movie_title = movie['title']

        movie_rate = movie['rate']
        movie_url = movie['url']
        movie_cover = movie['cover']
        movieinfo = '电影名：%s\n评分：%s\n电影地址：%s\n封面：%s\n' % (movie_title, movie_rate, movie_url, movie_cover)
        movies = movies + movieinfo + '\n'

    with open('%s.txt' % kind, 'w') as f:
        f.write(movies)

else:
    print '选择的影视种类有误,请核对后再次输入'
