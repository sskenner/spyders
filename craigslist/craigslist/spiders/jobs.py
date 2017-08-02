# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ["craigslist.org"]
    # allowed_domains = ['https://newyork.craigslist.org/search/egr']
    start_urls = ['https://newyork.craigslist.org/search/egr']

    def parse(self, response):
    	jobs = response.xpath('//p[@class="result-info"]')
    	for job in jobs:
    		title = job.xpath('a/text()').extract_first()
    		yield{'Title':title}