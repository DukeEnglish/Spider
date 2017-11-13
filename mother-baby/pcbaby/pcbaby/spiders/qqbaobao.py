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
    name = 'bozhongwang'


    def start_requests(self):
        urls = [
            'http://bbs.bozhong.com/forumall-2258-0-lastpost-0-0-0-2.html'
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
            for i in range (3,201):
                new_url = 'http://bbs.bozhong.com/forumall-2258-0-lastpost-0-0-0-'+str(i)+'.html'
                yield scrapy.Request(url = new_url, callback = self.parse)

    def parse(self, response):
        self.logger.info('parse begin, url=%s' % (response.url))
        page = response.body_as_unicode()
        sel = Selector(text = page)
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        article_links = sel.xpath("/html/body//tbody//div[@class='thread_info']//a/@href")
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        # print 'article_links=%s' % (article_links)

        for article_link in article_links:
            # print '我卡'
            # print article_link
            href = article_link.extract()
            # print href
            url = 'http://bbs.bozhong.com/%s' % (href)
            # print url 
            # print url
            # from scrapy.shell import inspect_response
            # inspect_response(response, self)
            yield scrapy.http.Request(url = url, callback = self.parse_list_page)


    def parse_list_page(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        self.logger.info('parse_list_page begin, url=%s' % (response.url))
        page = response.body_as_unicode()
        sel = Selector(text = page)
        p_list = sel.xpath("/html/body//div[@class='fsz_main']//td[@first='1']/text()")

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
