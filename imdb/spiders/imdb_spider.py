import os
from scrapy.spider import Spider
from scrapy.selector import Selector

from imdb.items import ImdbItem

class ImdbSpider(Spider):
    name = "imdb"
    allowed_domains = ["imdb.com"]
    path = os.path.join(os.path.dirname(__file__), "../movie_url.txt")
    f = open(path, 'r')
    text = f.readline()
    url = text.strip()
    start_urls = [
        url
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []
        item = ImdbItem()
        item['title'] = sel.xpath('//h1[@class="header"]/span[@class="itemprop"]/text()').extract()
        item['cast_information'] = sel.xpath('//div[@itemprop="actors"]/a/span/text()').extract()
        item['sypnosis'] = sel.xpath('//p[@itemprop="description"]/text()').extract()
        item['broadcast_date'] = sel.xpath('//div[@id="titleDetails"]/div/h4[text()="Release Date:"]/../text()').extract()
        item['production_company'] = sel.xpath('//div[@id="titleDetails"]/div/h4[text()="Production Co:"]/../span/a/span/text()').extract()
        return item
