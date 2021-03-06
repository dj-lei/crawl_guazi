from crawl_guazi.spiders import *


urls = {
        'baidu': 'https://www.baidu.com/',
        'get_cookie': 'https://m.guazi.com/cd/?ca_s=pz_baidu&ca_n=tbmkbturl'
        }


class SpiderAssembleDetail(scrapy.Spider):
    name = "assemble_detail"
    cookie = settings.COOKIES

    def start_requests(self):
        try:
            yield scrapy.Request(url=urls['get_cookie'], cookies=settings.COOKIES, callback=self.parse)
            yield scrapy.Request(url=urls['baidu'], callback=self.parse_null)

            while True:
                url = redis_con.spop('guazi_list')
                if url is None:
                    break
                yield scrapy.Request(url=url, cookies=self.cookie, callback=self.parse_list)

        except Exception as e:
            with configure_scope() as scope:
                scope.set_extra("spider_name", self.name)
                scope.set_extra("position", 'start_requests')
            capture_exception(e)

    def parse_null(self, response):
        pass

    def parse(self, response):
        """
        获取cookie
        """
        try:
            self.cookie = parse_cookies(self.cookie, response.headers.getlist('Set-Cookie'))
        except Exception as e:
            with configure_scope() as scope:
                scope.set_extra("url", response.url)
                scope.set_extra("crawl_content", response.body)
            capture_exception(e)

    def parse_list(self, response):
        try:
            tree = etree.HTML(response.body)

            # 判断是否有车源
            text_nocar = tree.xpath("//div[@class='tips--text_nocar']/text()")
            if len(text_nocar) > 0:
                print(text_nocar[0])
                return True

            find_num = tree.xpath("//div[@class='find-num bg-shadow active']/text()")[0]
            find_num = int(re.findall('(\d+)', find_num)[0])
            details = tree.xpath("//li[@class='list-item']/a/@href")
            for detail in details:
                url = 'https://m.guazi.com'+detail
                redis_con.sadd('guazi_details', url)

            for i in range(2, int(find_num/len(details))+1):
                t = time.time()
                now_time = lambda: int(round(t * 1000))
                url = response.url+'o'+str(i)+'/?act=getNext&timestamp='+str(now_time())
                if i > 50:
                    break
                yield scrapy.Request(url=url, cookies=self.cookie, callback=self.parse_get_next)
        except Exception as e:
            with configure_scope() as scope:
                scope.set_extra("url", response.url)
                scope.set_extra("crawl_content", response.body)
            capture_exception(e)

    def parse_get_next(self, response):
        try:
            tree = etree.HTML(str(json.loads(str(response.body, encoding="utf-8"))['data']['thisCity']))
            details = tree.xpath("//li[@class='list-item']/a/@href")

            for detail in details:
                url = 'https://m.guazi.com' + detail
                redis_con.sadd('guazi_details', url)
        except Exception as e:
            with configure_scope() as scope:
                scope.set_extra("url", response.url)
                scope.set_extra("crawl_content", response.body)
            capture_exception(e)

