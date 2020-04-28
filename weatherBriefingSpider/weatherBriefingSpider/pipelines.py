# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime

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
        now = datetime.datetime.now()
        date = str(now.year) + '年' + str(now.month) + '月'+str(now.day) + '日'
        img_name ='未定义.jpg'
        if request.meta['seq']==0:
            img_name = date+'-今日全国降水量预报图.jpg'
        if request.meta['seq']==1:
            img_name = date+'-明日全国降水量预报图.jpg'
        if request.meta['seq']==2:
            img_name = date+'-后天全国降水量预报图.jpg'
        return img_name

    # 返回item对象，给下一执行的管道类
    def item_completed(self, results, item, info):
        # 图片下载路径、url和校验和等信息
        print(results)
        return item