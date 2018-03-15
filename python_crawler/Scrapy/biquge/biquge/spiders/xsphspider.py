# -*- coding: utf-8 -*-
import scrapy
from biquge.items import BiqugeItem


class XsphspiderSpider(scrapy.Spider):
	name = 'xsphspider'
	allowed_domains = ['qu.la']
	start_urls = ['https://www.qu.la/book/4140/']

	def parse(self, response):
		chapters = response.xpath('//dd/a/@href').extract()

		for chapter in chapters:
			yield scrapy.Request("https://www.qu.la" + chapter, callback=self.get_text)

	def get_text(self, response):
		item = BiqugeItem()

		item['bookname'] = response.xpath('//div[@class="con_top"]/a[2]/text()').extract()[0]
		item['chapter_name'] = response.xpath('//h1/text()').extract()[0]

		novel_text = response.xpath('//div[@id="content"]/text()').extract()
		text = "".join(novel_text).strip().replace('\u3000','')
		item['body'] = text

		return item
