# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_l.settings import MOVIES,RPC

#class ScrapyLItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
#    pass

class mediagetItem(scrapy.Item):

    title = scrapy.Field()
    file_urls = scrapy.Field()
    processed_files = scrapy.Field()

    def get_info(self, type='link'):
        """
        :param type: 需要获取的类型
        :return: 该类型的list
        """
        return [ link[type] for link in MOVIES ]

    def query_info(self, name, type='link'):
        """
        :param name: 需要检索的名称
        :param type: 查询的类型
        :return: 返回list的第一个元素
        """
        return [ seq[type] for seq in MOVIES if seq['name'] == name][0]

    def get_rpc(self):
        return RPC
