from scrapy.selector import Selector
from pages.models import WebPage

class PagePipeline(object):

    def __init__(self):
        pass

    def process_item(self, item, spider):
        item.save()
        return item


class ParserPipeline(object):

    def __init__(self):
        pass

    def process_item(self, item, spider):
        record = WebPage.objects.get(url=item['url'])
        record.title = Selector(text=item['html']).xpath('//title/text()').extract()[0]
        record.save()
        return item
