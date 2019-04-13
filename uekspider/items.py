# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UekspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()     # 标题
    conlink = scrapy.Field()   # 内容链接
    con = scrapy.Field()       # 内容
    data = scrapy.Field()      # 时间
