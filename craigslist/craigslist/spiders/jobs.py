# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['https://newyork.craigslist.org/search/egr']
    start_urls = ['http://https://newyork.craigslist.org/search/egr/']

    def parse(self, response):
        pass
