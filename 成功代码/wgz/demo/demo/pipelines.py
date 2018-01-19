# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 导入数据库引擎对象
from sqlalchemy import create_engine
# 导入会话构建对象
from sqlalchemy.orm import sessionmaker
# 替换mysqldb模块
import pymysql
pymysql.install_as_MySQLdb()


class DemoPipeline(object):
    def process_item(self, item, spider):
        return item


class zhilianPipeline(object):
    '''
    处理智联招聘数据的pipeline，负责最终的数据验证和数据存储
    '''
    def __init__(self):
        '''
        初始化对象数据：可以用于初始化资源
        如：打开文件，打开数据库连接等等操作
        '''
        self.engine = create_engine('mysql://root:asd123@localhost/spider?charset=utf8')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def open_spider(self, spider):
        '''
        爬虫开启时需要调用的函数，经常用于数据初始化
        :param spider:
        :return:
        '''
        pass

    def close_spider(self, spider):
        '''
        爬虫程序关闭时自动调用的函数
        经常用于做一些资源回收的工作，如：关闭和数据的会话连接
        :param spider:
        :return:
        '''
        self.session.close()

    def process_item(self, item, spider):
        '''
        该函数会在爬虫采集并封装好Item对象时自动调用
        函数中针对item数据进行验证和储存
        :param item:
        :param spider:
        :return:
        '''
        print('>>>>>>>>>>>zhilian pipelines inworking >>>>>')
        # 定义sql语句
        sql = "insert into zhilian(job, company, money) values('%s', '%s', '%s')"%(item['job'], item['company'], item['money'])
        # 执行sql语句
        self.session.execute(sql)
        # 提交数据
        self.session.commit()


class neihanPipeline(object):

    def __init__(self):
        self.engine = create_engine('mysql://root:asd123@localhost/spider?charset=utf8')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        print('>>>>>>>>>>>>>>running>>>>>>>>>>>>')
        sql = "insert into neihan(username, createtime, content) values('%s', '%s', '%s')"%(item['username'], item['createtime'], item['content'])
        self.session.execute(sql)
        self.session.commit()
