# -*- coding: utf-8 -*-
import scrapy


class CharitiesSpider(scrapy.Spider):
    name = 'charities'
    allowed_domains = ['charityintelligence.ca']
    start_urls = ['https://www.charityintelligence.ca/research/a-z-charity-listing']

    def parse(self, response):
        pass
