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


class SpiderproPipeline(object):
    def process_item(self, item, spider):
        return item


class NeihanPipeline(object):

    def __init__(self):
        self.engine = create_engine('mysql://root:123456@localhost/py1709_spider?charset=utf8')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def open_spider(self,spider):
        pass

    def close_spider(self,spider):
        self.session.close()

    def process_item(self,item,spider):
        print (">>>>>>>>>runing>>>>>>")

        # 定义sql语句
        sql = "insert into neihan(username,createtime,content) values ('%s','%s','%s')" \
              % (item['username'], item['createtime'], item['content'])
        # 执行sql语句
        self.session.execute(sql)
        # 提交数据
        self.session.commit()

