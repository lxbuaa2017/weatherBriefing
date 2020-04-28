#爬虫
CURRENT_DIR=$(cd $(dirname $0); pwd)
cd weatherBriefingSpider
#如果之前运行过爬虫那么会存在brief.json，再次运行的话是会把内容追加在后面的，这样就不是准确的json格式了，会出错，所以要先删掉
if [ -f "brief.json" ];then
  rm -f brief.json
fi
scrapy crawl briefing -o brief.json -s FEED_EXPORT_ENCODING=UTF-8


#生成简报
cd $CURRENT_DIR/briefGenerator
python trainsition.py