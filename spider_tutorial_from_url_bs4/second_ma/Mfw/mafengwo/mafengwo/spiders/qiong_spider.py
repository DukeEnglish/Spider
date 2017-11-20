#!/bin/env python
#-*- encoding: utf-8 -*-


import re
import scrapy
from scrapy import Selector
import json
import urllib

def getHtml(url):
    html = urllib.urlopen(url).read()
    return html

def saveHtml(file_name, file_content):
    #    注意windows文件命名的禁用符，比如 /
    with open(file_name+'.html', "wb") as f:
        #   写文件用bytes而不是str，所以要转码
        f.write(file_content)


g_attri_pattern_cfg = {
    'p': re.compile('(?<=<p>).*(?=<\/p>)', re.U | re.M | re.S),
    'a': re.compile('<a.*?>', re.U | re.M | re.S),
    'strong': re.compile('(?<=<strong>).*(?=<\/strong>)', re.U | re.M | re.S),
}

dep =0
class mafengwoSpider(scrapy.Spider):
    name = 'qiongyou'
    dep =0
    def __init__(self, user_agent=''):
        self.user_agent = user_agent
    def start_requests(self):
        url = 'http://you.ctrip.com/sight/tokyo294/s0-p1.html'
        yield scrapy.Request(url = url, callback = self.parse)
        # for i in range (71):    
        #     new_url = 'http://you.ctrip.com/sight/tokyo294/s0-p'+str(i)+'.html#sightname'
        #     yield scrapy.Request(url = new_url, callback = self.parse)
        # for i in xrange(2,42):
        #     url = urls+'-1-'+str(i)
        #     yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        self.logger.info('parse begin, url=%s' % (response.url))
        page = response.body_as_unicode()
        from scrapy.shell import inspect_response
        inspect_response(response, self)
        sel = Selector(text=page)
        name_list = sel.xpath("html/body//li[@class ='item']")
        for name in name_list:
            print name.extract()
            # names = name.xpath(".//h3[@class = 'title YaHei']")
            # for n in names:
            #     print n.extract()
    # def parse_list_page(self, response):
    #     pass
    #     self.logger.info('parse_list_page begin, url=%s' % (response.url))
    #     page = response.body_as_unicode()
    #     sel = Selector(text = page)
    #     p_list = sel.xpath("/html/body//div[@class='art-text']/p")
    #     for p in p_list:
    #         text = p.extract()
    #         for k, re_obj in g_attri_pattern_cfg.items():
    #             if 'a' == k:
    #                 text = re_obj.sub('', text)
    #                 text = text.replace('</a>', '')
    #             else:
    #                 res = re_obj.search(text)
    #                 if res:
    #                     text = res.group()
    #         print 'doc=%s' % (text.encode('utf-8'))
