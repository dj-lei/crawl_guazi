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
            redis_con.sadd('guazi_list', url)


urls = {
        'baidu': 'https://www.baidu.com/',
        'get_cookie': 'https://m.guazi.com/cd/?ca_s=pz_baidu&ca_n=tbmkbturl',
        'city': 'https://m.guazi.com/ajax.php?dir=vehicle&module=GetSelectCity&pageType=list',
        'brand': 'https://m.guazi.com/cd/buy/?act=changeBrand'
        }


class SpiderAssembleList(scrapy.Spider):
    name = "assemble_list"
    cookie = settings.COOKIES

    def start_requests(self):
        try:
            yield scrapy.Request(url=urls['get_cookie'], cookies=settings.COOKIES, callback=self.parse)
            yield scrapy.Request(url=urls['baidu'], callback=self.parse_null)

            yield scrapy.Request(url=urls['brand'], cookies=self.cookie, callback=self.parse_brand)
            yield scrapy.Request(url=urls['city'], cookies=self.cookie, callback=self.parse_city)
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
            key = list(urls.keys())[list(urls.values()).index(response.url)]
            filename = root_path + '/tmp/' + key + '.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)
            self.cookie = parse_cookies(self.cookie, response.headers.getlist('Set-Cookie'))
        except Exception as e:
            with configure_scope() as scope:
                scope.set_extra("url", response.url)
                scope.set_extra("crawl_content", response.body)
            capture_exception(e)

    def parse_city(self, response):
        try:
            key = list(urls.keys())[list(urls.values()).index(response.url)]
            filename = root_path + '/tmp/'+key+'.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)

            self.cookie = parse_cookies(self.cookie, response.headers.getlist('Set-Cookie'))

            # 解析城市
            filename = root_path + '/tmp/'+key+'.html'
            with open(filename, 'r', encoding='utf-8') as f:
                city = f.read()

            result = pd.DataFrame()
            for first_alpha in json.loads(city)['allCityList'].keys():
                temp = pd.DataFrame(json.loads(city)['allCityList'][first_alpha])
                temp['first_alpha'] = first_alpha
                result = result.append(temp, sort=False)
            result = result.sort_values(by=['first_alpha']).reset_index(drop=True)
            result.to_csv(root_path + '/tmp/'+key+'.csv', index=False)
        except Exception as e:
            with configure_scope() as scope:
                scope.set_extra("url", response.url)
                scope.set_extra("crawl_content", response.body)
            capture_exception(e)

    def parse_brand(self, response):
        try:
            key = list(urls.keys())[list(urls.values()).index(response.url)]
            filename = root_path + '/tmp/'+key+'.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)

            self.cookie = parse_cookies(self.cookie, response.headers.getlist('Set-Cookie'))
            # 解析品牌
            f = codecs.open(root_path + '/tmp/'+key+'.html', "r", "utf-8")
            content = f.read()
            f.close()
            tree = etree.HTML(content)
            brand_url = tree.xpath("//div[@class='brand-rbox rel']/section/ul/li[@class=' js-change-brand']/@data-brandurl")
            brand_name = tree.xpath("//div[@class='brand-rbox rel']/section/ul/li[@class=' js-change-brand']/i/@alt")
            brand_url = pd.DataFrame(pd.Series(brand_url), columns=['brand_url'])
            brand_url['brand_name'] = pd.Series(brand_name)
            brand_url.to_csv(root_path + '/tmp/' + key + '.csv', index=False)

            # 组合list url到redis
            assemble_list()
        except Exception as e:
            with configure_scope() as scope:
                scope.set_extra("url", response.url)
                scope.set_extra("crawl_content", response.body)
            capture_exception(e)

