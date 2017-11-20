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


class mafengwoSpider(scrapy.Spider):
    name = 'mafengwo'
    dep =0
    def __init__(self, user_agent=''):
        self.user_agent = user_agent
    def start_requests(self):
        urls = [
            'http://www.mafengwo.cn/wenda/detail-1456433.html'
        ]
        for url in urls:
            param = re.findall(r"\d",url)
            param = ''.join(param)
            html = getHtml(url)
            saveHtml(param, html)# 保存种子网页
            for i in range(1032168,10000000,100):
                # url_real = response.url
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+1)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+2)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+3)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+4)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+5)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+6)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+7)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+8)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+9)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+10)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+11)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+12)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+13)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+14)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+15)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+16)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+17)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+18)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+19)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+20)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+21)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+22)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+23)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+24)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+25)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+26)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+27)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+28)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+29)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+30)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+31)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+32)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+33)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+34)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+35)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+36)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+37)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+38)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+39)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+40)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+41)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+42)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+43)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+44)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+45)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+46)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+47)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+48)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+49)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+50)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+51)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+52)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+53)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+54)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+55)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+56)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+57)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+58)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+59)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+60)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+61)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+62)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+63)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+64)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+65)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+66)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+67)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+68)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+69)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+70)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+71)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+72)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+73)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+74)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+75)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+76)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+77)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)

                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+78)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+79)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+80)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+81)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+82)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+83)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+84)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+85)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+86)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+87)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+88)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+89)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+90)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+91)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+92)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+93)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+94)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+95)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+96)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+97)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+98)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)
                url_real = 'http://www.mafengwo.cn/wenda/detail-'+str(i+99)+'.html'
                yield scrapy.Request(url = url_real, callback = self.parse)

    def parse(self, response):
        url_real = response.url
        param = re.findall(r"\d",url_real)
        param = ''.join(param)
        html = getHtml(url_real)
        saveHtml(param, html)