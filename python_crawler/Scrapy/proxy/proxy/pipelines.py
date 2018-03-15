# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
class ProxyPipeline(object):
    def process_item(self, item, spider):
		base_dir = os.getcwd()
		filename = base_dir + "/data/kuaidai_proxy.txt"
		with open(filename, 'a') as f:
			f.write(item['addr']+"\n")

		return item
