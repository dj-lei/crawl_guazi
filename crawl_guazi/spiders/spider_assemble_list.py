from crawl_guazi.spiders import *

urls = {
        'city': 'https://m.guazi.com/ajax.php?dir=vehicle&module=GetSelectCity&pageType=list',
        'brand': 'https://m.guazi.com/cd/buy/?act=changeBrand'
        }


class SpiderAssembleList(scrapy.Spider):
    name = "assemble_list"

    def start_requests(self):

        yield scrapy.Request(url=urls['city'], cookies=settings.COOKIES, callback=self.parse_city)

        yield scrapy.Request(url=urls['brand'], cookies=settings.COOKIES, callback=self.parse_brand)

    def parse_city(self, response):
        key = list(urls.keys())[list(urls.values()).index(response.url)]
        filename = root_path + '/tmp/'+key+'.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

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

    def parse_brand(self, response):
        key = list(urls.keys())[list(urls.values()).index(response.url)]
        filename = root_path + '/tmp/'+key+'.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        f = codecs.open(root_path + '/tmp/'+key+'.html', "r", "utf-8")
        content = f.read()
        f.close()
        tree = etree.HTML(content)
        brand_url = tree.xpath("//div[@class='brand-rbox rel']/section/ul/li[@class=' js-change-brand']/@data-brandurl")
        brand_name = tree.xpath("//div[@class='brand-rbox rel']/section/ul/li[@class=' js-change-brand']/i/@alt")
        brand_url = pd.DataFrame(pd.Series(brand_url), columns=['brand_url'])
        brand_url['brand_name'] = pd.Series(brand_name)
        brand_url.to_csv(root_path + '/tmp/' + key + '.csv', index=False)