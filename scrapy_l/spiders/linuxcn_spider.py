# -*- coding: utf-8 -*-

import scrapy
from scrapy_l.items import linuxcnItem

class linuxcnSpider(scrapy.Spider):
    name = "linuxcn"
    allowed_domains = ["linux.cn"]
    start_urls = [
        "https://linux.cn/tech/"
    ]

    def parse(self,response):
        for s in response.xpath('//ul/li'):
            title = s.xpath('a/text()').extract()
            link = s.xpath('a/@href').extract()
            desc = s.xpath('text()').extract()
            print(title,link,desc)
