import pymongo
import scrapy
from scrapy.conf import settings


class MongoPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        self.db = connection[settings['MONGODB_DB']]

    def process_item(self, item, spider):
        collection = self.db[item['url']]
        collection.insert(dict(item))
        return item

# class HtmlFilePipeline(object):
#     def process_item(self, item, spider):
#         file_name = item['url']
#         with open('files/%s.html' % file_name, 'w+b') as f:
#             f.write(item['html'])
