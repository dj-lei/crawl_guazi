from crawl_guazi.spiders import *

urls = {
        '常州_大众': 'https://m.guazi.com/changzhou/dazhong/'
        }


class SpiderAssembleDetail(scrapy.Spider):
    name = "assemble_detail"

    def start_requests(self):

        yield scrapy.Request(url=urls['常州_大众'], cookies=settings.COOKIES, callback=self.parse)

    def parse(self, response):
        try:
            tree = etree.HTML(response.body)
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
        except:
            filename = root_path + '/tmp/error.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)

    def parse_get_next(self, response):
        try:
            tree = etree.HTML(str(json.loads(str(response.body, encoding="utf-8"))['data']['thisCity']))
            details = tree.xpath("//li[@class='list-item']/a/@href")

            for detail in details:
                url = 'https://m.guazi.com' + detail
                redis_con.lpush('guazi_details', url)
        except:
            filename = root_path + '/tmp/error.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)