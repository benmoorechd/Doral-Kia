from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Doralkia(BasePortiaSpider):
    name = "www.doralkia.com"
    allowed_domains = [u'www.doralkia.com']
    start_urls = [u'https://www.doralkia.com/searchnew.aspx']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(PortiaItem, None, u'.col-md-9',
                   [Field(u'Year', 'div:nth-child(4)::attr(data-year)', [])])]]
