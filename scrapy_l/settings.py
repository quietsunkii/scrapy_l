# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_l project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_l'

SPIDER_MODULES = ['scrapy_l.spiders']
NEWSPIDER_MODULE = 'scrapy_l.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_l (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_l.middlewares.ScrapyLSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_l.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scrapy_l.pipelines.ScrapyLPipeline': 300,
#}

ITEM_PIPELINES = {'scrapy_l.pipelines.mediagetPipeline': 1}
FILES_STORE = '.\\downloads'
FILES_URLS_FIELD = 'file_urls'
FILES_RESULT_FIELD = 'processed_files'

MOVIES = [
    {'name': '生活大爆炸第十季/全集Season 10迅雷下载', 'link': 'http://cn163.net/archives/23809/', 'storge': '/home/cloud/tv/生活大爆炸 (2007)/Season 10'},
    {'name': '闪电侠第三季/全集Season 3迅雷下载', 'link': 'http://cn163.net/archives/23790/', 'storge': '/home/cloud/tv/The Flash (2014)/Season 3'},
    {'name': '神盾局特工第四季/全集Agents Of SHIELD迅雷下载', 'link': 'http://cn163.net/archives/23794/', 'storge': '/home/cloud/tv/神盾局特工 (2013)/Season 4'},
    {'name': '女超人第二季/全集Season 2迅雷下载', 'link': 'http://cn163.net/archives/24016/', 'storge': '/home/cloud/tv/SuperGirl (2016)/Season 2'},
    {'name': '明日传奇第二季/全集Legends of Tomorrow迅雷下载', 'link': 'http://cn163.net/archives/23814/', 'storge': '/home/cloud/tv/Legends of Tomorrow (2016)/Season 2'},
    {'name': '维京传奇第四季/全集Vikings迅雷下载', 'link': 'http://cn163.net/archives/19880/', 'storge': '/home/cloud/tv/维京传奇 (2013)/Season 4'},
]

RPC = {
    'address': '10.10.10.10',
    'port': '9091',
    'user': 'admin',
    'password': 'sy.sunkii0'
}

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5'
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
