### 环境配置
首先要有python3的环境
然后进入项目根目录，运行pip install -r requirements.txt

### 运行

## Linux系统下直接进入项目根目录，运行run.sh脚本即可

**Windows系统下具体操作为：**
进入到weatherBriefingSpider/weatherBriefingSpider目录，如果之前跑过爬虫目录下会有brief.json文件，有的话就先删掉
命令行执行 scrapy crawl briefing -o brief.json -s FEED_EXPORT_ENCODING=UTF-8 
将在该文件夹下生成brief.json


然后进入briefGenerator文件夹，运行python trainsition.py 
将会在项目根目录下生成"xxxx年x月xx日气象.docx" 文档

### 生成物

**简报文件**
项目根目录下的docx文件，其命名为“xxxx年xx月xx日气象”

**数据（即weatherBriefingSpider/brief.json文件）**
[{
	"brief_title": "吉林云南等地出现小雨 内蒙古辽宁等地升温明显",
	"brief_detail": "今天白天，全国大部地区降水较弱，吉林东部、云南西部等地的部分地区出现小雨；另外，内蒙古中部、辽宁辽东半岛等地的部分地区出现8～9级阵风。今14时较昨14时，内蒙中部和东南部、黑龙江东部、辽宁、河北中北部、山西、山东半岛、河南西部、江苏、安徽等地的部分地区出现4～6℃升温，内蒙古中部、辽宁西部以及江苏中部、安徽东部等局地升温8～10℃。",
	"key_point_title": ["云南多阴雨天气", "华北黄淮将有高温天气"],
	"key_point_detail": ["受低层切变系统影响，28日夜间至30日，云南等地有小雨，局地有中到大雨。此外,30日至5月2日，西南地区东部和江南等地有一次降水过程，部分地区有中到大雨，局地暴雨。28日夜间至5月2日，北方大部地区气温将继续回升，其中华北、黄淮气温大幅上升，升温幅度将达到6～8℃，局地可达10℃以上。预计30日至5月3日，华北东部和中南部、黄淮北部和西部的部分地区最高气温可达35～37℃。上述大部地区午后有4～6级阵风，其中，内蒙古、东北等地的部分地区可达7级左右。"],
	"day1_detail": "4月28日20时至29日20时，西藏中西部有小雪或雨夹雪；吉林东部、西藏东南部、西南地区北部和南部、海南岛、台湾岛等地部分地区有小到中雨，云南西部局地有大雨。内蒙古中西部、甘肃西部、华北东部、山东半岛等地部分地区有4～6级及以上风。",
	"day2_detail": "4月29日20时至30日20时，青海东南部、西藏南部等地的部分地区有小雪或雨夹雪；西南地区大部、江南西部以及吉林东部、辽宁北部、广西中东部、新疆伊犁河谷、西藏东南部等地有小到中雨，其中，重庆南部局地大雨（25～40毫米）。内蒙古东部、辽东半岛、黄淮北部等地的部分地区有4～6级风。",
	"day3_detail": "4月30日20时至5月1日20时，青海东南部、西藏中部和南部等地的部分地区有小雪或雨夹雪；江淮南部、江南大部、华南中部以及黑龙江北部、四川西部和南部、贵州大部、云南大部等地有小到中雨，其中，贵州中部、广西北部、湖南东北部、江西西北部等地的部分地区有大雨，局地暴雨（50～65毫米）。内蒙古中东部、东北地区中南部、华北东南部、黄淮东北部等地的部分地区有4～6级风。",
	"img_urls": ["http://image.nmc.cn/product/2020/04/28/WEBU/medium/SEVP_NMC_WEBU_SFER_EME_AGLB_LNO_P9_20200428180000000_XML_1.jpg?v=1588066036197", "http://image.nmc.cn/product/2020/04/28/WEBU/medium/SEVP_NMC_WEBU_SFER_EME_AGLB_LNO_P9_20200428180000000_XML_2.jpg?v=1588066036454", "http://image.nmc.cn/product/2020/04/28/WEBU/medium/SEVP_NMC_WEBU_SFER_EME_AGLB_LNO_P9_20200428180000000_XML_3.jpg?v=1588066036701"],
	"influence_and_concern": ["1. 4月29日至5月2日北方地区气温大幅上升，降水偏少，需做好森林草原和城镇防火气象服务；", "2. 云南持续阴雨天气，防范可能产生的地质灾害；", "3. 4月30日至5月2日江南、华南及贵州等地降雨过程。"]
}]


**图片**
存储在weatherBriefingSpider/weatherBriefingSpider/img中
其命名为"xxxx年xx月xx日-今日全国交通气象预报.png","xxxx年xx月xx日-明日全国交通气象预报.png","xxxx年xx月xx日-后天全国交通气象预报.png"

