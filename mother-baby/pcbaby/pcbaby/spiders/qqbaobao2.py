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
    name = 'qqbaobao2'


    def start_requests(self):
        urls = [
            'http://www.qqbaobao.com/xinshenger/baojianhuli/',
            'http://www.qqbaobao.com/xinshenger/mianyijiezhong/',
            'http://www.qqbaobao.com/xinshenger/changjianjibing/',
            'http://www.qqbaobao.com/xinshenger/zaochaner/',
            'http://www.qqbaobao.com/yingerjieduan/baojian/',
            'http://www.qqbaobao.com/yingerjieduan/muruweiyang/',
            'http://www.qqbaobao.com/yingerjieduan/rengongweiyang/',
            'http://www.qqbaobao.com/yingerjieduan/chengchangzhibiao/',
            'http://www.qqbaobao.com/yingerjieduan/fushitianjia/',
            'http://www.qqbaobao.com/yingerjieduan/mianyijiezhong/',
            'http://www.qqbaobao.com/yingerjieduan/changjianjibing/',
            'http://www.qqbaobao.com/yingerjieduan/yingerzaojiao/',
            'http://www.qqbaobao.com/youerjieduan/yingyang/',
            'http://www.qqbaobao.com/youerjieduan/baojian/',
            'http://www.qqbaobao.com/youerjieduan/xinli/',
            'http://www.qqbaobao.com/youerjieduan/jiaoyu/',
            'http://www.qqbaobao.com/youerjieduan/youerhuli/',
            'http://www.qqbaobao.com/youerjieduan/youerweiyang/',
            'http://www.qqbaobao.com/youerjieduan/chengchangzhibiao/',
            'http://www.qqbaobao.com/youerjieduan/youerjibing/',
            'http://www.qqbaobao.com/youerjieduan/youeranquan/',
            'http://www.qqbaobao.com/youerjieduan/rutuoxuzhi/',
            'http://www.qqbaobao.com/xueqianjieduan/yingyang/',
            'http://www.qqbaobao.com/xueqianjieduan/baojian/',
            'http://www.qqbaobao.com/xueqianjieduan/xinli/',
            'http://www.qqbaobao.com/baobaowendang/qinbaohuodong/',
            'http://www.qqbaobao.com/xueqianjieduan/chengchangzhibiao/',
            'http://www.qqbaobao.com/xueqianjieduan/hulibaojian/',
            'http://www.qqbaobao.com/xueqianjieduan/changjianjibing/',
            'http://www.qqbaobao.com/xueqianjieduan/caiyipeiyang/',
            'http://www.qqbaobao.com/xueqianjieduan/zhilikaifa/',
            'http://www.qqbaobao.com/xueqianjieduan/ertonganquan/',
            'http://www.qqbaobao.com/xueqianjieduan/ruyuanzhunbei/',
            'http://www.qqbaobao.com/xueqianjieduan/xingjiaoyu/',
            'http://www.qqbaobao.com/xueqianjieduan/youxiwanju/'
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
                # print next_url
                # print '下一页'

    def parse_list_page(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        # pass
        self.logger.info('parse_list_page begin, url=%s' % (response.url))
        page = response.body_as_unicode()
        sel = Selector(text = page)
        p_list = sel.xpath("/html/body//div[@class='a-main-n']/p/text()")

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
