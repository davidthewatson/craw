from scrapy_djangoitem import DjangoItem
from pages.models import WebPage


class PageItem(DjangoItem):
    django_model = WebPage
