import scrapy

from ..items import LomparsScrapeItem


class LomparsSpider(scrapy.Spider):
    name = 'lompars'
    allowed_domains = ['победа-63.рф']
    start_urls = ['http://победа-63.рф/']

    def start_requests(self):
        start_point = 'https://победа-63.рф/catalog/kompyuternaya-tehnika/noutbuki/1/?q=60'
        last_page = 51

        urls = [
            'https://победа-63.рф/catalog/kompyuternaya-tehnika/noutbuki/1/?q=60',
            'https://победа-63.рф/catalog/kompyuternaya-tehnika/noutbuki/2/?q=60',
            'https://победа-63.рф/catalog/kompyuternaya-tehnika/noutbuki/3/?q=60',
            'https://победа-63.рф/catalog/kompyuternaya-tehnika/noutbuki/4/?q=60',
            'https://победа-63.рф/catalog/kompyuternaya-tehnika/noutbuki/48/?q=60',
            'https://победа-63.рф/catalog/kompyuternaya-tehnika/noutbuki/49/?q=60',
            'https://победа-63.рф/catalog/kompyuternaya-tehnika/noutbuki/50/?q=60',
            'https://победа-63.рф/catalog/kompyuternaya-tehnika/noutbuki/51/?q=60',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        items = response.xpath('//div[@class="card-content"]')
        for element in items:
            item = LomparsScrapeItem()
            item['title'] = element.xpath('.//meta[@itemprop="name"]/@content')[0].get()
            item['price'] = element.xpath('.//div[@class="card-price"]/@content')[0].get()
            item['link'] = element.xpath('.//a[@class="card-title"]/@href')[0].get()
            yield item
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
