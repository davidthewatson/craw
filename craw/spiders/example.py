import scrapy
from scrapy.linkextractors import LinkExtractor
from craw.items import PageItem


class BlogSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['http://davidwatson.org/']

    def parse(self, response):
        item = PageItem()
        extractor = LinkExtractor(allow_domains='davidwatson.org')
        links = extractor.extract_links(response)
        item['url'] = response.url
        item['html'] = response.body
        item['links'] = [link.url for link in links]
        for link in links:
            yield scrapy.Request(link.url, callback=self.parse)
        yield item
