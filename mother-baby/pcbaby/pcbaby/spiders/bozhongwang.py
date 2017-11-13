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
    name = 'qqbaobao'


    def start_requests(self):
        urls = [
            'http://www.qqbaobao.com/zhunbeihuaiyun/baojian/',
            'http://www.qqbaobao.com/zhunbeihuaiyun/xinli/',
            'http://www.qqbaobao.com/zhunbeihuaiyun/buyun/',
            'http://www.qqbaobao.com/zhunbeihuaiyun/yunqianzhunbei/',
            'http://www.qqbaobao.com/zhunbeihuaiyun/huaiyunjinji/',
            'http://www.qqbaobao.com/zhunbeihuaiyun/shengnanshengnv/',
            'http://www.qqbaobao.com/zhunbeihuaiyun/youshengyouyu/',
            'http://www.qqbaobao.com/zhengzaihuaiyun/yingyang/',
            'http://www.qqbaobao.com/zhengzaihuaiyun/baojian/',
            'http://www.qqbaobao.com/zhengzaihuaiyun/taijiao/',
            'http://www.qqbaobao.com/zhengzaihuaiyun/huaiyuntezheng/',
            'http://www.qqbaobao.com/zhengzaihuaiyun/taierfayu/',
            'http://www.qqbaobao.com/zhengzaihuaiyun/yunqijiancha/',
            'http://www.qqbaobao.com/zhengzaihuaiyun/changjianjibing/',
            'http://www.qqbaobao.com/zhengzaihuaiyun/yunqianquan/',
            'http://www.qqbaobao.com/zhengzaihuaiyun/liuchanzaochan/',
            'http://www.qqbaobao.com/zhengzaihuaiyun/yunqishenghuo/',
            'http://www.qqbaobao.com/fenmianqianhou/yingyang/',
            'http://www.qqbaobao.com/fenmianqianhou/baojian/',
            'http://www.qqbaobao.com/fenmianqianhou/chanqianxuzhi/',
            'http://www.qqbaobao.com/fenmianqianhou/zhunbeidaichan/',
            'http://www.qqbaobao.com/fenmianqianhou/fenmianguocheng/',
            'http://www.qqbaobao.com/fenmianqianhou/chanhoujibing/',
            'http://www.qqbaobao.com/fenmianqianhou/chanhoushoushen/',
            'http://www.qqbaobao.com/hangyexinwen/',
            'http://www.qqbaobao.com/xinshenger/muruweiyang/',
            'http://www.qqbaobao.com/xinshenger/rengongweiyang/',
            'http://www.qqbaobao.com/xinshenger/chengchangzhibiao/'
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
            # for i in range (3,201):
            #     new_url = 'http://bbs.bozhong.com/forumall-2258-0-lastpost-0-0-0-'+str(i)+'.html'
            #     yield scrapy.Request(url = new_url, callback = self.parse)

    def parse(self, response):
        self.logger.info('parse begin, url=%s' % (response.url))
        page = response.body_as_unicode()
        sel = Selector(text = page)
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        article_links = sel.xpath("/html/body//div[@class='list_d']/dl")
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        # print 'article_links=%s' % (article_links)

        for article_link in article_links:
            # print '我卡'
            # print article_link
            href = article_link.xpath("./dt/a/@href").extract()
            # print href
            url = '%s' % (href)[0]
            # print url 
            # print url
            # from scrapy.shell import inspect_response
            # inspect_response(response, self)
            yield scrapy.http.Request(url = url, callback = self.parse_list_page)
        next_urls = sel.xpath("/html/body//div[@class='paginating']/ul/li")
        # print '我是测试'
        # print next_urls
        if next_urls:
            for next_url in next_urls:
                # print next_url.xpath("./a/text()").extract()[0]
                if next_url.xpath("./a/text()").extract()[0]==u'下一页':
                    yield scrapy.http.Request(url = next_url.xpath("./a/@href").extract()[0], callback = self.parse)
                    # print next_url.xpath("./a/@href").extract()[0]
                    # print '下一页'

    def parse_list_page(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        # pass
        self.logger.info('parse_list_page begin, url=%s' % (response.url))
        page = response.body_as_unicode()
        sel = Selector(text = page)
        p_list = sel.xpath("/html/body//div[@class='a-main-n']/p/text()")
        # print "我叫测试"
        # print response.url

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
