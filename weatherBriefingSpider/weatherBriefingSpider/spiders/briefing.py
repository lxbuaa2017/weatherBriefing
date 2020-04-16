# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.selector import Selector
import re

class BriefingSpider(scrapy.Spider):
    name = 'briefing'
    allowed_domains = ['http://www.nmc.cn']
    start_urls = ['http://www.nmc.cn/publish/weather-bulletin/index.htm']

    def start_requests(self):
        yield Request(self.start_urls[0], callback=self.parse)

    # response已经加载了气象公报网页，parse的工作是抽取信息
    def parse(self, response):
        sel = Selector(response)
        # 抽取重点天气预报，获得一个数组
        strs = sel.xpath("/html/body/div[@class='container']/div[@class='row']/div[@class='col-xs-10']/div[@class='bgwhite'][2]/div[@id='text']/div[@class='writing']/p//text()").extract()
        # 第一步先把无关信息去掉
        img_anotation_rz = r'（见图[1-9]）'
        for i,str in enumerate(strs):
            # 删去“图5 全国降水量预报图（4月18日08时-19日08时）”等图片标题
            if(str[0]=='图'):
                strs.remove(str)
            # 去掉(见图x)
            strs[i] = re.sub(img_anotation_rz, "", strs[i])
        # 删去最后一句“制作： 徐成鹏 孟庆涛                   签发： 方翀”
        strs.remove(strs[-1])
        with open("test.txt", "w") as f:
            for str in strs:
                f.write(str+'\n')
        pass
