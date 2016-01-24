# -*- coding: utf-8 -*-
import scrapy
from upwork.items import UpworkItem
    

class JobSpider(scrapy.Spider):
	name = 'jobs'
	upworkDomain = 'https://www.upwork.com'
	start_urls = [
			"https://www.upwork.com/o/jobs/browse/c/web-mobile-software-dev/",
		]

	def parse(self, response):
		for jobs in response.xpath('//article[contains(@class,"job-tile js-similar-tile")]'):
			#print jobs.extract()
			item = UpworkItem()
			item['title'] = jobs.xpath('.//a[contains(@class,"break visited")]/text()').extract()
			item['description'] = jobs.xpath('.//div[contains(@class,"description")]//div/text()').extract()
			item['postTime'] = jobs.xpath('.//time/@datetime').extract()
			item['skills'] = jobs.xpath('.//a[contains(@class,"o-tag-skill")]//span/text()').extract()
			yield item

		for href in response.xpath('//div//a[contains(@o-log-page,"search_navigation_bottom_next")]/@href'):
			next_url = self.upworkDomain+href.extract()
			print next_url
			yield scrapy.Request(next_url)
