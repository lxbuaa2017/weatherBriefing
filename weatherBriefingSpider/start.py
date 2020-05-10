import os
import cmd
import time


cmd1="scrapy crawl briefing -o ./weatherBriefingSpider/brief.json -s FEED_EXPORT_ENCODING=UTF-8"
cmd2="python ../briefGenerator/trainsition.py"
cmd3="python ../briefGenerator/connect_mongodb.py"


os.remove("./weatherBriefingSpider/brief.json")
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)