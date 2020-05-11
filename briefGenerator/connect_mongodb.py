# -*- coding: utf-8 -*-
from pymongo import MongoClient
import time
import json
import os
import sys
from bson.binary import Binary
import base64
from PIL import Image


jsonFile = open("../weatherBriefingSpider/weatherBriefingSpider/brief.json",mode="r",encoding="utf-8")

jsonLoad = json.load(jsonFile)

client = MongoClient('192.144.229.202',27017)
cur=date= time.strftime('%Y{y}%m{m}%d{d}',time.localtime(time.time())).format(y='年',m='月',d='日')

onepicUrl = "../weatherBriefingSpider/weatherBriefingSpider/img/"+cur+"-今日全国降水量预报图.png"
twopicUrl = "../weatherBriefingSpider/weatherBriefingSpider/img/"+cur+"-明日全国降水量预报图.png"
threepicUrl="../weatherBriefingSpider/weatherBriefingSpider/img/"+cur+"-后天全国降水量预报图.png"

onePic = ""
twoPic = ""
threePic = ""
if os.path.exists(onepicUrl):
    onePic = base64.b64encode(open(onepicUrl,mode="rb").read())
if os.path.exists(twopicUrl):
    twoPic = base64.b64encode(open(twopicUrl,mode="rb").read())
if os.path.exists(threepicUrl):
    threePic = base64.b64encode(open(threepicUrl,mode="rb").read())

db = client['python-db']
col = db['Weather']
image={'onepic':'','twopic':'','threepic':''}
aim={'name':'','document':'','image':image}
aim["name"]=cur
aim["document"]=jsonLoad[0]
aim["image"]["onepic"]= onePic
aim["image"]["twopic"] = twoPic
aim["image"]["threepic"]= threePic

#col.delete_many({})

col.insert_one(aim)

for item in col.find(): 
    picdata = item["image"]["threepic"]
    with open('1.png', 'wb') as file:
        data = base64.b64decode(picdata)  
        file.write(data)  