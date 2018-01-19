# -*- coding:utf-8 -*-
__author__ = 'wgz'
__date__ = '2018/1/10 15:44'

import requests

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 爬虫开始时间
import datetime
start_time = datetime.datetime.now()
# 获取要查询信息
news_type = raw_input('请输入要获取的新闻类型(XX新闻)：')
news_page_num = raw_input('请输入从第几页获取新闻：')
news_num = raw_input('请输入要获取的新闻条数：')
# news_type = raw_input('请输入要获取的新闻类型(XX新闻)：')
# 对新闻提取首字母
def multi_get_letter(str_input):
  if isinstance(str_input, unicode):
    unicode_str = str_input
  else:
    try:
      unicode_str = str_input.decode('utf8')
    except:
      try:
        unicode_str = str_input.decode('gbk')
      except:
        print 'unknown coding'
        return
  return_list = []
  for one_unicode in unicode_str:
    return_list.append(single_get_first(one_unicode))
  return return_list
def single_get_first(unicode1):
  str1 = unicode1.encode('gbk')
  try:
    ord(str1)
    return str1
  except:
    asc = ord(str1[0]) * 256 + ord(str1[1]) - 65536
    if asc >= -20319 and asc <= -20284:
      return 'a'
    if asc >= -20283 and asc <= -19776:
      return 'b'
    if asc >= -19775 and asc <= -19219:
      return 'c'
    if asc >= -19218 and asc <= -18711:
      return 'd'
    if asc >= -18710 and asc <= -18527:
      return 'e'
    if asc >= -18526 and asc <= -18240:
      return 'f'
    if asc >= -18239 and asc <= -17923:
      return 'g'
    if asc >= -17922 and asc <= -17418:
      return 'h'
    if asc >= -17417 and asc <= -16475:
      return 'j'
    if asc >= -16474 and asc <= -16213:
      return 'k'
    if asc >= -16212 and asc <= -15641:
      return 'l'
    if asc >= -15640 and asc <= -15166:
      return 'm'
    if asc >= -15165 and asc <= -14923:
      return 'n'
    if asc >= -14922 and asc <= -14915:
      return 'o'
    if asc >= -14914 and asc <= -14631:
      return 'p'
    if asc >= -14630 and asc <= -14150:
      return 'q'
    if asc >= -14149 and asc <= -14091:
      return 'r'
    if asc >= -14090 and asc <= -13119:
      return 's'
    if asc >= -13118 and asc <= -12839:
      return 't'
    if asc >= -12838 and asc <= -12557:
      return 'w'
    if asc >= -12556 and asc <= -11848:
      return 'x'
    if asc >= -11847 and asc <= -11056:
      return 'y'
    if asc >= -11055 and asc <= -10247:
      return 'z'
    return ''
def main(str_input):
  a = multi_get_letter(str_input)
  b = ''
  for i in a:
    b= b+i
  return b
new_type = main(news_type)

# 包装headers不裸奔
headers = {
    'User-agent':'Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10 (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2'
}

# 设置代理
proxies = {
    'https':'183.52.150.128:61234',
    'http':'115.226.9.2:3128'
}


# 获取最新时间戳实时获取最新新闻
import time
time_stamp = int(time.time())*1000
print time_stamp
# get请求参数
get_param = {
    'channel': 'news', # 类型
    # 'cat_1': 'shxw', # 新闻类型
    'level==1||': '2', #
    'show_ext': 1,
    'show_all': 1,
    'show_num': news_num, # 每页新闻条数
    'tag': 1,
    'format': 'json', # 数据格式
    'page': news_page_num, # 第几页
    #'callback': 'newsloadercallback', # 返回值储存元组名称
    '_': time_stamp, # 时间戳
}
# 请求链接不同的地方
if news_type == 'shxw':
    get_param['cat_2==zqsk||=qwys||=shwx||'] = 'fz-shyf'
elif news_type == 'gnxw':
    get_param['cat_2==gdxw1||=gatxw||=zs-pl||'] = 'mtjj'
get_param['cat_1'] = new_type

url = 'http://api.roll.news.sina.com.cn/zt_list?'
response = requests.get(url, params=get_param, headers=headers, proxies=proxies)
news_text = response.text

# 解析json字符串
import json
json_dict = json.loads(news_text)
data = json_dict['result']['data']

# 创建文件夹
import os
# os.mkdir('./%s'%news_type.decode('utf-8').encode('gbk'))

# for 遍历取值
dir_name = news_type.decode('utf-8').encode('gbk')
for news_one in data:
    file_name = news_one['title'].decode('utf-8').encode('gbk')
    with open('./%s/%s.txt'%(dir_name, file_name), 'w') as f:
        f.write(news_one['title'].encode('utf-8')+news_one['createtime'].encode('utf-8'))

# 爬虫结束时间
end_time = datetime.datetime.now()

# 文件大小
file_list = os.listdir('./%s'%dir_name)
dir_size = sum(map(lambda x:os.path.getsize('./%s/%s'%(dir_name, x)),[file for file in file_list]))
print('文件大小：%sk'%dir_size)
# 爬取时间
use_time = end_time-start_time
print('爬虫+写入消耗时间：{}s'.format(use_time.seconds))
