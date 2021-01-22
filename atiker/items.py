# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AtikerItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    lang = scrapy.Field()
