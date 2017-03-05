# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import transmissionrpc
import re
import glob
from scrapy.pipelines.files import FilesPipeline

class mediagetPipeline(FilesPipeline):
    def process_item(self, item, spider):
        rpc = item.get_rpc()
        # 初始化rpc接口
        tc = transmissionrpc.Client(address=rpc['address'], port=rpc['port'], user=rpc['user'], password=rpc['password'])
        download_dir = item.query_info(item['title'],type='storge')

        for link in item['file_urls']:
            #判断文件是否存在
            if self._check_file(link,download_dir):
                tc.add_torrent(link,download_dir=download_dir)
        return item

    #def get_media_requests(self, item, info):
    #    pass

    def _check_file(self, link, dir):
        match = 'S\d{2}E\d{2}'
        name = re.findall(match,link)
        # 获取所有mkv文件
        mkvs = glob.glob(dir + r'/*.mkv')
        for n in mkvs:
            if name == re.findall(match,n):
               return False
        return True

    #def item_completed(self, results, item, info):
    #   pass

