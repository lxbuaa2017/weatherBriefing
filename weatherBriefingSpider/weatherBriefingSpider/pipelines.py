# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class WeatherbriefingspiderPipeline(object):
    def process_item(self, item, spider):
        return item

class WeatherImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for i in range(0,3):
            url = item["img_urls"][i]
            yield scrapy.Request(url,meta={'seq':i})

    # 指定文件存储路径
    def file_path(self, request, response=None, info=None):
        # 打印图片路径
        # print(request.url)
        # 通过分割图片路径获取图片名字
        img_name = request.meta['seq']
        return img_name

    # 返回item对象，给下一执行的管道类
    def item_completed(self, results, item, info):
        # 图片下载路径、url和校验和等信息
        print(results)
        return item