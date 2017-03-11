# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import transmissionrpc
import re
import os
import glob
import requests
from scrapy.http import request
from scrapy.pipelines.files import FilesPipeline
from lxml.html import etree


class mediagetPipeline(FilesPipeline):
    """处理下载链接等"""

    def process_item(self, item, spider):
        """处理下载链接
        :param item: spider返回的信息
        :param spider: spider名
        :return:
        """
        rpc = item.get_rpc()
        # 初始化rpc接口
        tc = transmissionrpc.Client(address=rpc['address'], port=rpc['port'], user=rpc['user'], password=rpc['password'])
        download_dir = item.query_info(item['title'],type='storge')
        for link in item['file_urls']:
            #判断文件是否存在
            if self._check_file(link,download_dir):
                to = tc.add_torrent(link,download_dir=download_dir)
                try:
                    
                    self._download_subtitle(to.name, download_dir)
                finally:
                    pass
        return item

    def _check_file(self, link, dir):
        """ 检测本地文件是否存在
        :param link: 下载链接
        :param dir: 本地目录
        :return: 是否存在
        """
        match = 'S\d{2}E\d{2}'
        name = re.findall(match,link)
        # 获取所有mkv文件
        mkvs = glob.glob(dir + '/' + r'*')
        for n in mkvs:
            if name == re.findall(match,n):
               return False
        return True

    #
    def _download_subtitle(self, searchstr, savedir):
        """
        :param searchstr: 查找字符串
        :param savedir: 保存的目录
        :return:
        """
        head = {
            #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
             'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5'
        }

        searchstr = searchstr.replace('[rartv]','[rarbg]')
        #print(searchstr)
        c = re.search('.*(?=\[rarbg\])', searchstr)
        
        if c:
            # 默认按热度排序
            search_link = 'http://assrt.net/sub/?searchword=' + c.group() + '&sort=relevance&no_redir=1'
            r = requests.request('GET', search_link, headers=head)
            htree = etree.HTML(r.content)
            short_link = htree.xpath('//div[@class="resultcard"]/div[@class="subitem"]/div/span/a/@href')[0]

            search_link = 'http://assrt.net' + short_link
            r = requests.request('GET', search_link, headers=head)
            htree = etree.HTML(r.content)
            link = htree.xpath('//span[@id="detail-filelist"]/div/@onclick')[0]

            link = re.findall('"(.*?)"', link)
            link.insert(1, '-')
            filedir = savedir + '/' +searchstr
            filename = filedir + '/' + link[-1]
            link = "/".join(list(link))

            down_link = 'http://assrt.net/download/' + link
            r = requests.get(down_link, stream=True, headers=head)

            if not os.path.exists(filedir):
                os.mkdir(filedir)
            with open(filename, 'wb') as fd:
                for chunk in r.iter_content(4096):
                    fd.write(chunk)

            return True
        return False


