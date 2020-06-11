from __future__ import absolute_import

import scrapy
from collections import defaultdict
from scrapy.loader.processors import Join, MapCompose, Identity
from w3lib.html import remove_tags
from .utils.processors import Text, Number, Price, Date, Url, Image


class PortiaItem(scrapy.Item):
    fields = defaultdict(
        lambda: scrapy.Field(
            input_processor=Identity(),
            output_processor=Identity()
        )
    )

    def __setitem__(self, key, value):
        self._values[key] = value

    def __repr__(self):
        data = str(self)
        if not data:
            return '%s' % self.__class__.__name__
        return '%s(%s)' % (self.__class__.__name__, data)

    def __str__(self):
        if not self._values:
            return ''
        string = super(PortiaItem, self).__repr__()
        return string


class CarsForSaleMiamiFlDoralKia1Item(PortiaItem):
    Transmission = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Certified = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Model = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    MSRP = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    VIN = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Sale_Price = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    field1 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    MPG_Highway = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Exterior_Color = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Make = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Bodystyle = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    MPG_City = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Fuel_Type = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Interior_Color = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Stock = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Condition = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Image = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    Full_Title = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Model_Code = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Engine = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Year = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Trim = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class CarsForSaleMiamiFlDoralKiaItem(PortiaItem):
    Image = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
    field2 = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
