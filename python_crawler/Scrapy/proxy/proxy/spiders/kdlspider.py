# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem


class KdlspiderSpider(scrapy.Spider):
	name = 'kdlspider'
	allowed_domains = ['kuaidaili.com']
	start_urls = []
	for i in range(1,6):
		url = "https://kuaidaili.com/free/inha/%s/" % str(i)
		start_urls.append(url)

	def parse(self, response):
		item = ProxyItem()
		match_list=response.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
		for match in match_list:
			ipaddr = match.xpath('td/text()').extract()[0]
			port = match.xpath('td/text()').extract()[1]
			item['addr'] = ipaddr + ":" + port

			yield item
