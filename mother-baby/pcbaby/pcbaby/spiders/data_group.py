#!/bin/env python
#-*- encoding: utf-8 -*-


import re
import scrapy
from scrapy import Selector
import json


g_attri_pattern_cfg = {
    'p': re.compile('(?<=<p>).*(?=<\/p>)', re.U | re.M | re.S),
    'a': re.compile('<a.*?>', re.U | re.M | re.S),
    'strong': re.compile('(?<=<strong>).*(?=<\/strong>)', re.U | re.M | re.S),
}


class PcbabySpider(scrapy.Spider):
    name = 'test_for'

    def start_requests(self):
        urls = [
            'https://izhongchou.taobao.com/dream/ajax/getProjectList.htm?page=2&pageSize=20&projectType=121288001&type=6&status=&sort=1'            
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)


    def parse(self, response):
        self.logger.info('parse begin, url=%s' % (response.url))
        data = json.loads(response.body)
        for datum in data:

            url = datas["link"]
            print url