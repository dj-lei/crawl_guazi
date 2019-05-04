# -*- coding: utf-8 -*-

# Scrapy settings for crawl_guazi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'crawl_guazi'

SPIDER_MODULES = ['crawl_guazi.spiders']
NEWSPIDER_MODULE = 'crawl_guazi.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawl_guazi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
}

COOKIES = {'__51cke__': '',
             '__51laig__': '25',
             '__tins__19717059': '%7B%22sid%22%3A%201556167156491%2C%20%22vd%22%3A%2011%2C%20%22expires%22%3A%201556169284336%7D',
             '__utmganji_v20110909': 'd534f7ec-4388-40b0-f480-262956732220',
             'antipas': '542085B2026i7rdF59y6O02u3z',
             'cainfo': '%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%222%22%2C%22version%22%3A1%2C%22ca_i%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%221904b_qgg3qi%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%229606d532-e781-476c-d085-020dc5ca8e29%22%2C%22sessionid%22%3A%2281969045-a5fc-4c32-9761-7b10f4161611%22%7D',
             'chg_city': '1',
             'cityDomain': 'changzhou',
             'cityGuideInfo': '2019-4-25%231',
             'cityGuideVersion': 'B',
             'clueSourceCode': '%2A%2300',
             'ganji_uuid': '3697923462868752433136',
             'lg': '1',
             'list_url': '%2Fchangzhou%2Fdazhong%2F',
             'lng_lat': '0',
             'preTime': '%7B%22last%22%3A1556167305%2C%22this%22%3A1555912819%2C%22pre%22%3A1555912819%7D',
             'sessionid': '81969045-a5fc-4c32-9761-7b10f4161611',
             'user_city_id': '69',
             'uuid': '9606d532-e781-476c-d085-020dc5ca8e29',
             'zg_7e763bc025fc4122af64893d9f28969f': '%7B%22sid%22%3A%201556167156608%2C%22updated%22%3A%201556167489896%2C%22info%22%3A%201555913186355%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22m.guazi.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22landHref%22%3A%20%22https%3A%2F%2Fm.guazi.com%2Fchangzhou%2Fdazhong%2F%22%7D',
             'zg_did': '%7B%22did%22%3A%20%2216a43a71c1ff2-05c4b61f3b87c6-2e634637-4a574-16a43a71c22bc%22%7D'
           }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'crawl_guazi.middlewares.CrawlGuaziSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'crawl_guazi.middlewares.CrawlGuaziDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'crawl_guazi.pipelines.CrawlGuaziPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = '/tmp/httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
