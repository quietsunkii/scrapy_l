#### 这是学习scrapy的练习，在github上做个备份 ####
## 使用方法 ##
打开scrapy_l/settings.py，填写MOVIES字段及RPC参数。

MOVIES共有3个参数
- name：剧集的名字，该名字为cn163.net中剧集页的标题。
- link：剧集页地址
- storge：该剧集存储的位置，请使用绝对路径


例：
```
MOVIES = [
    {
      'name': '生活大爆炸第十季/全集Season 10迅雷下载', 
      'link': 'http://cn163.net/archives/23809/', 
      'storge': '/media/tv/生活大爆炸 (2007)/Season 10/'
     }
]
```
RPC共有4个参数


- address：transmissionrpc的IP
- port：rpc的端口，默认是9091
- user：如果设置了认证，填入用户名
- password：对应用户的密码
