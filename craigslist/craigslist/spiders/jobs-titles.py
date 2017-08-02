# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ["craigslist.org"]
    # allowed_domains = ['https://newyork.craigslist.org/search/egr']
    start_urls = ['https://newyork.craigslist.org/search/egr']

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        for title in titles:
        	yield {'Title': title}
