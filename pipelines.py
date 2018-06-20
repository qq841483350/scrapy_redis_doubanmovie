# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import DoubanItem
from scrapy.conf import  settings
import pymongo

class DoubanPipeline(object):
    def __init__(self):
        host=settings['MONGODB_HOTS']
        port=settings['MONGODB_PORT']
        dbName=settings['MONGODB_DBNAME']
        docName=settings['MONGODB_DOCNAME']
        conn=pymongo.MongoClient(host=host,port=port)
        db=conn[dbName]  #连接数据库
        self.post_info=db[docName]

    def process_item(self, item, spider):
        movieInfo=dict(item)  #将item转化为一个字典
        self.post_info.insert(movieInfo)  #插入数据库
        return item
