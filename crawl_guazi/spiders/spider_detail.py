from crawl_guazi.spiders import *


def check_contain_chinese(check_str):
    for ch in check_str:
        if (u'\u4e00' <= ch <= u'\u9fff') | (ch.isdigit()):
            return True
    return False


def clean_list(labels):
    for i, label in enumerate(labels):
        if check_contain_chinese(label):
            labels[i] = labels[i].replace(' ', '')
        else:
            labels.pop(i)
    return labels


class SpiderDetail(scrapy.Spider):
    name = "detail"

    def start_requests(self):
        count = redis_con.llen('guazi_details')
        if count != 0:
            for i in range(0, count):
                url = redis_con.blpop('guazi_details', timeout=5)
                yield scrapy.Request(url=url[1], cookies=settings.COOKIES, callback=self.parse)

    def parse(self, response):
        try:
            tree = etree.HTML(response.body)

            car_source = pd.DataFrame(index=[0])
            car_source['url'] = response.url
            car_source['detail_name'] = tree.xpath("//h1[@class='product-title']/text()")[1].replace('\n', '').replace('  ', '')

            labels = tree.xpath("//section[@class='comm-area']/div[1]/div/ul/li/span/text()")
            values = tree.xpath("//section[@class='comm-area']/div[1]/div/ul/li/p/text()")
            labels = clean_list(labels)
            values = clean_list(values)
            doc = dict(zip(labels, values))

            car_source['year'] = doc['上牌时间']
            car_source['mile'] = doc['表显里程']
            car_source['city'] = doc['归属地']
            car_source['color'] = doc['车身颜色']
            car_source['price'] = float(tree.xpath("//span[@class='normal-price']/text()")[0])
            car_source['transfer_owner'] = doc['过户次数']
            car_source['annual_insurance'] = doc['年检到期时间']
            car_source['compulsory_insurance'] = doc['交强险到期时间']
            car_source['business_insurance'] = doc['商业险到期时间']
            car_source['description'] = tree.xpath("//span[@class='report-con']/text()")[1]
            car_source['description_time'] = tree.xpath("//span[@class='report-con']/text()")[0]
            car_source['region'] = doc['看车方式']
            car_source['create_time'] = datetime.datetime.now()

            db_operate.insert_car_source(car_source)
        except:
            filename = root_path + '/tmp/error.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)