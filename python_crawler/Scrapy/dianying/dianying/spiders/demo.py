# -*- coding: utf-8 -*-
import scrapy
from dianying.items import DianyingItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['dianying.2345.com/top']
    start_urls = ['http://dianying.2345.com/top/']

    def parse(self, response):
		#date=response.xpath("/html/body/div[2]/div/div[2]/div[1]/ul/li[1]/div[2]/p[1]/span[2]/text()").extract()[0]
		date=response.xpath('//ul[@class="picList clearfix"]/li[1]/div[2]/p[1]/span[2]/text()').extract()[0]
		items={}
		items["First"]=date

		return items
        
