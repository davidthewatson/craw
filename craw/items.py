from scrapy.item import Item, Field


class Listing(Item):
    url = Field()
    html = Field()
    links = Field()
