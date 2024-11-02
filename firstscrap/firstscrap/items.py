# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    Book_name=scrapy.Field()
    Price=scrapy.Field()
    Rating=scrapy.Field()
