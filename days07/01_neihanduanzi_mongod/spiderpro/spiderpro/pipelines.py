# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#引入数据库引擎对象
from sqlalchemy import create_engine
#导入会话构建对象
from sqlalchemy.orm import sessionmaker
#替换mysqldb模块
import pymysql
pymysql.install_as_MySQLdb()

import pymongo

class SpiderproPipeline(object):
    def process_item(self, item, spider):
        return item

class NeiHanPipeline(object):

    def __init__(self):
        # #使用mysql数据库
        # self.engine = create_engine("mysql://root:123456@localhost/py1709_spider?charset=utf8")
        # Session = sessionmaker(bind=self.engine)
        # self.session = Session()

        #使用mongodb进行连接
        client = pymongo.MongoClient("localhost",27017)
        self.sess = client['py1709_spider']['neihan']

    def open_spider(self,spider):
        pass

    def close_spider(self,spider):
        pass

        # self.session.close()

    def process_item(self,item,spider):
        print('>>>>>>>>>>>>>runing>>>>....')

        data = {
            'username':item['username'],
            'createtime':item['createtime'],
            'content':item['content']
        }

        self.sess.insert(data)

        # #定义sql语句
        # sql = "insert into nhdz(username,createtime,content) VALUES ('%s','%s','%s')" \
        # %(item['username'],item['createtime'],item['content'])
        #
        # #执行sql语句
        # self.session.execute(sql)
        # #提交数据
        # self.session.commit()

