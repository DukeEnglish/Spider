#!/bin/env python
#-*- encoding: utf-8 -*-


import re
import scrapy
from scrapy import Selector



g_attri_pattern_cfg = {
    'p': re.compile('(?<=<p>).*(?=<\/p>)', re.U | re.M | re.S),
    'a': re.compile('<a.*?>', re.U | re.M | re.S),
    'strong': re.compile('(?<=<strong>).*(?=<\/strong>)', re.U | re.M | re.S),
}


class PcbabySpider(scrapy.Spider):
    name = 'q_baby'
    
    def start_requests(self):
        urls = [
            'http://www.babytree.com/ask/myqa__view~mlist,tab~B',
            'http://www.babytree.com/ask/myqa__view~mlist,tab~D',
            'http://www.babytree.com/ask/myqa__view~mlist,tab~zero',
            'http://www.babytree.com/ask/myqa__view~mlist,tab~mobile'
        ]
        for url in urls:
            for i in range(1,251):
                next_url = url+',pg~'+str(i)
            #next_url = 'http://www.babytree.com' + next_url[8]
                # print next_url
            
                yield scrapy.Request(url = next_url, callback = self.parse)
            

    def parse(self, response): # find the first level: a list for each baike
        
        # recorde.append(response.url)
        self.logger.info('parse begin, url=%s' % (response.url))
        page = response.body_as_unicode()
        sel = Selector(text = page) # the elements we want have different 
        
        item_list = sel.xpath("/html/body//li[@class='list-item']")# get the suffix of a link 
        
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
            

        #print 'item_list=%s' % (item_list)
        for item in item_list:# get the speific link based on the suffix of link
            #
            # //*[@id="divQuestionList"]/ul/li[1]/div/p
            text = item.xpath(".//p[@class='list-title']/a/text()")
        

            text = text.extract()[0]
            print text.encode('utf-8')

        next_url = response.xpath("/html/body//div[@class='pagejump']/a/@href").extract()
        # print '我是事实'
        # print next_url
        # print len(recorde)
        

