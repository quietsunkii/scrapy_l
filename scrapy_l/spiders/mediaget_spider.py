# -*- coding: utf-8 -*-

import scrapy,re
from scrapy_l.items import mediagetItem

class mediagetSpider(scrapy.Spider):
    name = "mediaget"
    #allowed_domains = ["cn163.net"]

    def start_requests(self):
        item = mediagetItem()
        for url in item.get_info():
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        item = mediagetItem()
        item['title'] = response.xpath('//h2[@class="entry_title"]/text()').extract_first()
        links =[]
        files =[]
        for s in response.xpath('//div[@id="entry"]/p/a'):
            name = s.xpath('text()').extract_first()
            # 正则匹配文件名：S03E06.720P.mkv
            # 过滤需要的视频
            if re.match('^S\d{2}E\d{2}.720P.mkv',name):
                link = s.xpath('@href').extract_first()
                filename = re.findall('dn=(\S*?)%',link)
                links.append(link)
                files.append(filename)
        item['file_urls'] = links
        #item['processed_files']= files
        yield item

