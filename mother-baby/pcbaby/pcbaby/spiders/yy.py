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
    name = 'yybaby'

    def start_requests(self):
        urls = [
            'http://www.babyschool.com.cn/article/syht/index.php?page=',
            'http://www.babyschool.com.cn/article/jkbb/index.php?page='
        ]
        for url in urls:
            for i in range(1,1001):
                _url = url+str(i)
                yield scrapy.Request(url = _url, callback = self.parse)


    def parse(self, response):
        self.logger.info('parse begin, url=%s' % (response.url))
        page = response.body_as_unicode()
        sel = Selector(text = page)
        article_links = sel.xpath("/html/body//div[@class='comiis_wzli cl']")
        # print 'article_links=%s' % (article_links)
        for article_link in article_links:
            href = article_link.xpath(".//li[@class='wzbt']/a/@href").extract()
            

            url = 'http://www.babyschool.com.cn/%s' % (href[0])
            # print url
            yield scrapy.http.Request(url = url, callback = self.parse_list_page)

    def parse_list_page(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        self.logger.info('parse_list_page begin, url=%s' % (response.url))
        page = response.body_as_unicode()
        sel = Selector(text = page)
        p_list = sel.xpath("/html/body//p/span/text()")

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
            print '%s' % (text.encode('utf-8'))
