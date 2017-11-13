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
    name = 'pcbaby'

    def start_requests(self):
        urls = [
            'http://baike.pcbaby.com.cn/yunqian.html',
            'http://baike.pcbaby.com.cn/yunqi.html',
            'http://baike.pcbaby.com.cn/fenmian.html',
            'http://baike.pcbaby.com.cn/yuezi.html',
            'http://baike.pcbaby.com.cn/xinshenger.html',
            'http://baike.pcbaby.com.cn/yinger.html',
            'http://baike.pcbaby.com.cn/youer.html',
            'http://baike.pcbaby.com.cn/xuelingqian.html',
            'http://baike.pcbaby.com.cn/meishi.html',
            'http://baike.pcbaby.com.cn/shenghuo.html',
            'http://baike.pcbaby.com.cn/yongpin.html',
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        self.logger.info('parse begin, url=%s' % (response.url))
        page = response.body_as_unicode()
        sel = Selector(text = page)
        bk_list = sel.xpath("/html/body//div[@class='baike-tb clearfix']")
        print 'bk_list=%s' % (bk_list)
        for tb in bk_list:
            a_attri = tb.xpath("./div[@class='baike-tb-dl']//dd/span/a")
            for item in a_attri:
                href = item.xpath("./@href").extract()
                url = 'http:%s' % (href[0])
                yield scrapy.http.Request(url = url, callback = self.parse_list_page)

    def parse_list_page(self, response):
        self.logger.info('parse_list_page begin, url=%s' % (response.url))
        page = response.body_as_unicode()
        sel = Selector(text = page)
        p_list = sel.xpath("/html/body//div[@class='art-text']/p")
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
