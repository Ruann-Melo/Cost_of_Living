# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CostOfLivingItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass


class HousingItem(scrapy.Item):
    headline = scrapy.Field()
    price = scrapy.Field()
    period = scrapy.Field()
    address = scrapy.Field()
    area = scrapy.Field()
    rooms = scrapy.Field()
    bathrooms = scrapy.Field()
    garage = scrapy.Field()
    link = scrapy.Field()
    city = scrapy.Field()