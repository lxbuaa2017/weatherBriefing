# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 重点天气预报:key_point
# 未来第一天具体预报:day1_detailed
# 未来第一天图片:day1_img_src
# 未来第二天具体预报:day2_detailed
# 未来第二天图片:day2_img_src
# 未来第三天具体预报:day3_detailed
# # 未来第三天图片:day3_img_src

class WeatherbriefingspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    key_point = scrapy.Field()
    day1_detailed = scrapy.Field()
    # day1_img_src = scrapy.Field()
    day2_detailed = scrapy.Field()
    # day2_img_src = scrapy.Field()
    day3_detailed = scrapy.Field()
    # day3_img_src = scrapy.Field()
    img_urls = scrapy.Field()
    images = scrapy.Field()
    pass
