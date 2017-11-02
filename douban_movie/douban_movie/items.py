# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
'''
# 
scraping的主要目标是从非结构性的资源中（网页）提取结构化数据。scrapy 爬虫可以以某种格式（例如python的dict）返回提取后的数据
python的dict缺少结构性。在fieldname和返回的非连续性的数据上面，比较容易出现typo的问题，特别是在一个有很多spider的工程中。

所以为了定义更佳常见的输出数据格式，scrapy就提供了item类。Item的对象是一个简单的容器，可以被用来收集scrapy到的数据。他们提供了
像字典一样的api，并且有方便语法来声明他们的作用域

多种多样的scrapy组件用到了item所提供的额外的信息。
输出看起来像是声明域，来区分输出的列。可以用item field的元数据来自定义序列化。
追踪器追踪item的事例来帮助内容缝隙等

The main goal in scraping is to extract structured data from unstructured sources, 
typically, web pages. 
Scrapy spiders can return the extracted data as Python dicts. 
While convenient and familiar, Python dicts lack structure: 
it is easy to make a typo in a field name or return inconsistent data, especially in a larger project with many spiders.

# To define common output data format Scrapy provides the Item class. 
Item objects are simple containers used to collect the scraped data. 
They provide a dictionary-like API with a convenient syntax for declaring their available fields.


# Various Scrapy components use extra information provided by Items: 
exporters look at declared fields to figure out columns to export, 
serialization can be customized using Item fields metadata, 
trackref tracks Item instances to help find memory leaks (see Debugging memory leaks with trackref), etc.

'''
import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()

    pass
