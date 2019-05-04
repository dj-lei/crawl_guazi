from crawl_guazi.spiders import *


def assemble_list():
    """
    组合list
    """
    head = 'https://m.guazi.com/'
    city = pd.read_csv(root_path + '/tmp/city.csv')
    brand = pd.read_csv(root_path + '/tmp/brand.csv')
    # 清空数据库
    redis_con.flushdb()
    for i in range(0, len(city)):
        city_domain = city['domain'][i]
        for j in range(0, len(brand)):
            brand_url = brand['brand_url'][j]
            url = head + city_domain + '/' + brand_url + '/'
            redis_con.lpush('guazi_list', url)


class SpiderAssembleDetail(scrapy.Spider):
    name = "assemble_detail"

    def start_requests(self):
        try:
            # assemble_list()

            count = redis_con.llen('guazi_list')
            if count != 0:
                for i in range(0, 30):
                    url = redis_con.blpop('guazi_list', timeout=5)
                    yield scrapy.Request(url=url[1], cookies=settings.COOKIES, callback=self.parse)
        except Exception as e:
            with configure_scope() as scope:
                scope.set_extra("spider_name", self.name)
                scope.set_extra("position", 'start_requests')
            capture_exception(e)

    def parse(self, response):
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
                redis_con.lpush('guazi_details', url)

            for i in range(2, int(find_num/len(details))+1):
                t = time.time()
                now_time = lambda: int(round(t * 1000))
                url = response.url+'o'+str(i)+'/?act=getNext&timestamp='+str(now_time())
                if i > 50:
                    break
                yield scrapy.Request(url=url, cookies=settings.COOKIES, callback=self.parse_get_next)
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
                redis_con.lpush('guazi_details', url)
        except Exception as e:
            with configure_scope() as scope:
                scope.set_extra("url", response.url)
                scope.set_extra("crawl_content", response.body)
            capture_exception(e)

