# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class SztianqiSpider(scrapy.Spider):
    name = 'SZtianqi'
    allowed_domains = ['suzhou.tianqi.com']
    start_urls = ['http://suzhou.tianqi.com/']

    def parse(self, response):
		items = []

		for day in xrange(1,8):
			item = WeatherItem()
		
			path='//ul[@class="week"]/li[%d]/b/text()' % day	
			item['date'] = response.xpath(path).extract()[0]

			path='//ul[@class="week"]/li[%d]/span/text()' % day	
			item['week'] = response.xpath(path).extract()[0]

			path='//ul[@class="week"]/li[%d]/img/@src' % day	
			item['img'] = response.xpath(path).extract()[0]

			path='//div[@class="zxt_shuju"]/ul/li[%d]/b/text()' % day	
			temp_low = response.xpath(path).extract()[0]
			path='//div[@class="zxt_shuju"]/ul/li[%d]/span/text()' % day	
			temp_high = response.xpath(path).extract()[0]
			item['temp'] = temp_low + "-" + temp_high + "'c"

			path='//ul[@class="txt txt2"]/li[%d]/text()' % day	
			item['weather'] = response.xpath(path).extract()[0]
			path='//ul[@class="txt"]/li[%d]/text()' % day	
			item['wind'] = response.xpath(path).extract()[0]

			items.append(item)

		return items

