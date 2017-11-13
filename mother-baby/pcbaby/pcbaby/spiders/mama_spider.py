#!/bin/env python
#-*- encoding: utf-8 -*-


import re
import scrapy
from scrapy import Selector
from pcbaby.items import mamaItem


g_attri_pattern_cfg = {
    'p': re.compile('(?<=<p>).*(?=<\/p>)', re.U | re.M | re.S),
    'a': re.compile('<a.*?>', re.U | re.M | re.S),
    'strong': re.compile('(?<=<strong>).*(?=<\/strong>)', re.U | re.M | re.S),
}


class PcbabySpider(scrapy.Spider):
    name = 'mamababy'
    
    def start_requests(self):
        urls = [
            'http://www.mama.cn/z/t674/',
            'http://www.mama.cn/z/t675/',
            'http://www.mama.cn/z/t1181/',
            'http://www.mama.cn/z/t1182/',
            'http://www.mama.cn/z/t1183/',
            'http://www.mama.cn/z/t666/',
            'http://www.mama.cn/z/t1184/',
            'http://www.mama.cn/z/t665/',
            'http://www.mama.cn/z/t20001/',
            'http://www.mama.cn/z/t20021/',
            'http://www.mama.cn/z/t200319/',
            'http://www.mama.cn/z/t200237/',
            'http://www.mama.cn/z/t200246/',
            'http://www.mama.cn/z/t200250/',
            'http://www.mama.cn/z/t200256/',
            'http://www.mama.cn/z/t3001/',
            'http://www.mama.cn/z/t3002/',
            'http://www.mama.cn/z/t3003/',
            'http://www.mama.cn/z/t3004/',
            'http://www.mama.cn/z/t3005/',
            'http://www.mama.cn/z/t200363/',
            'http://www.mama.cn/z/t200367/',
            'http://www.mama.cn/z/t200335/',
            'http://www.mama.cn/z/t200340/',
            'http://www.mama.cn/z/t200346/',
            'http://www.mama.cn/z/t200371/',
            'http://www.mama.cn/z/t200376/',
            'http://www.mama.cn/z/t200390/',
            'http://www.mama.cn/z/t200393/'
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
            

    def parse(self, response): # find the first level: a list for each baike
        self.logger.info('parse begin, url=%s' % (response.url))
        page = response.body_as_unicode()
        sel = Selector(text = page) # the elements we want have different 
        
        item_list = sel.xpath("/html/body//div[@class='cate-itemList']")# get the suffix of a link 

        name = sel.xpath("/html/body//div[@class='cate-item']/h5/a/text()").extract()[0]
     
        print 'name=%s' % (name.encode('utf-8'))  
        #output["catagory"] = name


        print 'item_list=%s' % (item_list)
        for item in item_list:# get the speific link based on the suffix of link
            a_attri = item.xpath("./h5/a")
            b_attri = item.xpath("./div[@class='common-list']//li/a")
            #a_attri = item.xpath("./div[@class='baike-tb-dl']//dd/span/a")
            href = a_attri.xpath("./@href").extract()# fetch the link the specific page 
            #url = 'http:%s' % (href[0])# construct a new url
            url = '%s' % (href[0])
            #print url
            #break
            yield scrapy.http.Request(url = url, callback = self.parse_list_page) # parse each url in the list. 
            #break

            for it in b_attri:
                href = it.xpath("./@href").extract()# fetch the link the specific page
                #url = 'http:%s' % (href[0])# construct a new url
                url = '%s' % (href[0])
                #print "我才是呢"
                #print url
                #url = 'http:%s' % (href[0])# construct a new url
                yield scrapy.http.Request(url = url, callback = self.parse_list_page) # parse each url in the list. 

    def parse_list_page(self, response): # I get the url of a page here is the problem
        self.logger.info('parse_list_page begin, url=%s' % (response.url))
        #print response
        page = response.body_as_unicode()
        #print page
        sel = Selector(text = page)
        #print sel
        t_p_list = sel.xpath("/html/body//div[@class='detail-mod J_floor']")
        #print "我是不是中文"
        #print t_p_list
        t = t_p_list.xpath("./div[@class='mod-title']//a/text()")
        #print t
        p_list = t_p_list.xpath("./div[@class='mod-ctn']//p")

        text = t.extract()[0]
        # print "我是中文"
        # print text
        for k, re_obj in g_attri_pattern_cfg.items():
            if 'a' == k:
                text = re_obj.sub('', text)
                text = text.replace('</a>', '')
            else:
                res = re_obj.search(text)
                if res:
                    text = res.group()
        print 'doc=%s' % (text.encode('utf-8'))
        #output["text"]=text.encode('utf-8')
        for p in p_list:
            text = p.extract()
            for k, re_obj in g_attri_pattern_cfg.items():
                if 'a' == k:
                    text = re_obj.sub('', text)
                    text = text.replace('</a>', '')
                else:
                    res = re_obj.search(text)
                    if res:
                        text = res.group()
            print 'doc=%s' % (text.encode('utf-8'))
            #output["text"]=text.encode('utf-8')
