# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.selector import Selector
from weatherBriefingSpider.items import WeatherbriefingspiderItem
import re


class BriefingSpider(scrapy.Spider):
    name = 'briefing'
    allowed_domains = ['www.nmc.cn']
    start_urls = ['http://www.nmc.cn/publish/weather-bulletin/index.htm']

    def start_requests(self):
        yield Request(self.start_urls[0], callback=self.parse)

    # response已经加载了气象公报网页，parse的工作是抽取信息
    def parse(self, response):
        sel = Selector(response)
        # 抽取重点天气预报，获得一个数组
        strs = sel.xpath(
            "/html/body/div[@class='container']/div[@class='row']/div[@class='col-xs-10']/div[@class='bgwhite'][2]/div[@id='text']/div[@class='writing']/p//text()").extract()
        # 第一步先把无关信息去掉
        img_anotation_rz = r'（见图[1-9]）'
        for i, str in enumerate(strs):
            # 删去“图5 全国降水量预报图（4月18日08时-19日08时）”等图片标题
            if str[0] == '图':
                strs.remove(str)
            # 去掉(见图x)
            strs[i] = re.sub(img_anotation_rz, "", strs[i])
        # 删去最后一句“制作： 徐成鹏 孟庆涛                   签发： 方翀”
        strs.remove(strs[-1])
        # 第一部分
        brief_title = strs[0]
        strs.remove(strs[0])
        brief_detail = ""
        index = 0
        for i, str in enumerate(strs):
            if str[0:2] != "二、":
                brief_detail += str
            else:
                index = i
                break
        strs = strs[index+1:]
        # 第二部分
        key_point_title = []
        key_point_detail = []
        index = 0
        detail = ""
        while strs[index][0:2] != "三、":
            if strs[index][1] == '.':
                if len(key_point_detail)!=0:
                    key_point_detail.append(detail)
                    detail = ""
                key_point_title.append(strs[index][2:])
            else:
                detail += strs[index]
            index += 1
        key_point_detail.append(detail)
        strs = strs[index+1:]
        #第三部分
        index = 0
        date_rz = r'[0-9]{1,2}月[0-9]{1,2}日'
        day1_detail = strs[index]
        index+=1
        while not re.search(date_rz, strs[index]):
            day1_detail+=strs[index]
            index+=1
        day2_detail = strs[index]
        index+=1
        while not re.search(date_rz, strs[index]):
            day2_detail+=strs[index]
            index+=1
        day3_detail = strs[index]
        index+=1
        # ！！！！！！！！！！！！！！！！！！！！！！！
        # 这里得注意是否一定有”四、“，会不会有时候没有？
        while not strs[index][1]=='、':
            day3_detail+=strs[index]
            index+=1
        # 第四部分
        strs = strs[index+1:]
        influence_and_concern = strs
        #爬取三张图片
        urls = sel.xpath("/html/body/div[@class='container']/div[@class='row']/div[@class='col-xs-10']/div[@class='bgwhite'][2]/div[@id='text']/div[@class='writing']/div/img/@src").extract()
        # 取最后三张图
        img_urls = urls[-4:-1]

        # 生成item
        item = WeatherbriefingspiderItem()
        item['brief_title'] = brief_title[2:]
        item['brief_detail'] = brief_detail
        item['key_point_title'] = key_point_title
        item['key_point_detail'] = key_point_detail
        item['day1_detail'] = day1_detail
        item['day2_detail'] = day2_detail
        item['day3_detail'] = day3_detail
        item['img_urls'] = img_urls
        item['influence_and_concern'] = influence_and_concern

        # with open("test.txt", "w") as f:
        #     for str in strs:
        #         f.write(str + '\n')
        # pass
        yield item