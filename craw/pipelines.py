from bs4 import BeautifulSoup
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
        soup = BeautifulSoup(item['html'], 'lxml')
        record.title = soup.title.text
        record.save()
        return item
