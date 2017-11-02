# coding: utf-8

from scrapy.spider import Spider

class douban_spider(Spider):

	name = 'douban_spider'
	start_urls = ["http://woodenrobot.me"]

	def parse(self,response):
		titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
		for title in titles:
			print title
