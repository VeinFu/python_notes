# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
class BiqugePipeline(object):
	def process_item(self, item, spider):
		base_dir = os.getcwd()
		chapter_content = base_dir + "/data/" + item['bookname'] + "_" + item['chapter_name'] + ".txt"

		with open(chapter_content, 'a') as f:
			f.write(item['body'].encode('utf-8'))

		return item
