# -*- coding: utf-8 -*-
import json
import jieba
import jieba.posseg as posseg
jieba.load_userdict("dict.txt")
with open('../weatherBriefingSpider/brief.json','r',encoding='utf-8') as fObj:
    raw_list = json.load(fObj)
    raw = raw_list[0]
    # for i, v in enumerate(raw['key_point_title']):
    #     kpt_seg = jieba.lcut(raw['key_point_title'][i])
    #     print(kpt_seg)
    for i,v in enumerate(raw['key_point_detail']):
        ked_sentences = raw['key_point_detail'][i].split("。")
        for ked_sentence in ked_sentences:
            ked_seg = posseg.lcut(ked_sentence)
            for pair in ked_seg:
                # 词语中含有大、暴并且是名词,这里注意“中到大雨”等jieba词典里没有，要自己加，亲测添加“中到大”不可以，添加“中到大雨”、“中到大雾”才行
                if ('大' in str(pair.word) or '暴' in str(pair.word))  and str(pair.flag) =='n':
                    print(pair.word)
                    print(ked_sentence+'\n')
                # if(str(pair.flag) =='north'):
                #     print(pair.word) //可用于自定义词典归纳地名，如华北地区、西北地区在dict.txt中词性都为north，可归纳为north(北方地区)
                    break
