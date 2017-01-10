import scrapy
from scrapy.conf import settings


class PagePipeline(object):

    def __init__(self):
        pass

    def process_item(self, item, spider):
        item.save()
        return item

# class HtmlFilePipeline(object):
#     def process_item(self, item, spider):
#         file_name = item['url']
#         with open('files/%s.html' % file_name, 'w+b') as f:
#             f.write(item['html'])
