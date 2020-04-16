# -*- coding: utf-8 -*-
import scrapy


class BriefingSpider(scrapy.Spider):
    name = 'briefing'
    allowed_domains = ['http://www.nmc.cn']
    start_urls = ['http://http://www.nmc.cn/']

    def parse(self, response):
        pass
