首先要有python3的环境
然后pip（或者conda） install scrapy
然后进入到/weatherBriefing/weatherBriefingSpider目录，
命令行执行 scrapy crawl briefing -o brief.json -s FEED_EXPORT_ENCODING=UTF-8 即可
