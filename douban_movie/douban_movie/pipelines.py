# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
当item被爬虫爬取到之后，被送到item pipeline里面。而这个item pipeline会通过序列化处理的几个组件来对item进行处理
After an item has been scraped by a spider, it is sent to the Item Pipeline which processes it through several components that are executed sequentially.
每一个item pipeline的组件是一个python类，并且执行了一个简单的方法。他们接受到一个item并且在这个item上面执行一个动作，并且决定这个item是否要继续经过这个item pipeline，还是说drop掉不再处理
Each item pipeline component (sometimes referred as just “Item Pipeline”) is a Python class that implements a simple method. They receive an item and perform an action over it, also deciding if the item should continue through the pipeline or be dropped and no longer processed.

对item pipeline的典型用法有：
清洗html数据
验证scraped到的数据（检查item是否包含有特定的field）
检查是否有重复（去重）
将爬取到的数据存储到database中

Typical uses of item pipelines are:

cleansing HTML data
validating scraped data (checking that the items contain certain fields)
checking for duplicates (and dropping them)
storing the scraped item in a database

'''


class DoubanMoviePipeline(object):
    def process_item(self, item, spider):
        return item
