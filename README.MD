
## 使用方法 ##
打开scrapy_l/settings.py，填写MOVIES字段及RPC参数。

MOVIES共有3个参数
- name：剧集的名字，该名字为cn163.net中剧集页的标题。
- link：剧集页地址
- storge：该剧集存储的位置，请使用绝对路径


例：
MOVIES = [
    {
      'name': r'生活大爆炸第十季/全集Season 10迅雷下载', 
      'link': 'http://cn163.net/archives/23809/', 
      'storge': '/home/cloud/tv/生活大爆炸 (2007)/Season 10/'
     }
]
