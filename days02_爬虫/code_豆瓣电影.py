# coding=utf-8
import urllib2
import urllib
import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')


url = 'https://movie.douban.com/j/search_subjects'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"
}

kinds = ["热门","最新","经典","可播放","豆瓣高分","冷门佳片","华语","欧美","韩国","日本","动作","喜剧","爱情","科幻","悬疑","恐怖","治愈"]

print '可供选择的影视类型：<热门>、<最新>、<经典>、\n' \
      '<可播放>、<豆瓣高分>、<冷门佳片>、<华语>、\n' \
      '<欧美>、<韩国>、<日本>、<动作>、<喜剧>、\n' \
      '<爱情>、<科幻>、<悬疑>、<恐怖>、<治愈>'

kind=raw_input('请选择影视类型：')
if kind in kinds:
    nums=raw_input('请输入您要获取的影视数量：')

    fromdata = {
        "type":"movie",
        "tag":kind	,
        "page_limit":nums,
        "page_start":"0",
    }

    data = urllib.urlencode(fromdata)
    request = urllib2.Request(url,data=data,headers=headers)
    response = urllib2.urlopen(request).read()
    moviejson = json.loads(response)
    movielist = moviejson['subjects']
    kind = (kind+'电影').decode('utf-8').encode('gbk')
    movies = ''
    for movie in movielist:
        movie_title = movie['title']

        movie_rate = movie['rate']
        movie_url = movie['url']
        movie_cover = movie['cover']
        movieinfo = '电影名：%s\n评分：%s\n电影地址：%s\n封面：%s\n'%(movie_title,movie_rate,movie_url,movie_cover)
        movies = movies+movieinfo+'\n'

    with open('%s.txt'%kind,'w') as f:
        f.write(movies)

else:
    print '选择的影视种类有误,请核对后再次输入'
