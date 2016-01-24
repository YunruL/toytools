# -*- coding: utf-8 -*-

import pymongo
from scrapy.exceptions import DropItem

class SavePipeline(object):

	collection_name = 'upwork_jobs'

	def __init__(self, mongo_uri, mongo_db):
		self.mongo_uri = mongo_uri
		self.mongo_db = mongo_db

	@classmethod
	def from_crawler(cls, crawler):
		return cls(
				mongo_uri = crawler.settings.get('MONGO_URI'),
				mongo_db = crawler.settings.get('MONGO_DATABASE', 'items')
			)

	def open_spider(self, spider):
		if self.mongo_uri == '':
			self.client = pymongo.MongoClient()
		else:
			self.client = pymongo.MongoClient(self.mongo_uri)
		self.db = self.client[self.mongo_db]

	def close_spider(self, spider):
		self.client.close()

	def process_item(self, item, spider):
		if item['postTime'][0][0] != '2':
			raise DropItem("not a valid record %s" %item['postTime'][0])
		else:
			item['description'] = map(lambda i: i.strip(), item['description'])
			item['title'] = map(lambda i: i.strip(), item['title'])
			self.db[self.collection_name].insert(dict(item))
			return item
