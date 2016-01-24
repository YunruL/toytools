from upwork.spiders.job_spider import JobSpider

# scrapy api
from scrapy import signals
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings

def spider_closing(spider):
    #Activates on spider closed signal
    print 'finished'
    reactor.stop()

settings = Settings()

# crawl responsibly
settings.set("USER_AGENT", "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
settings.set("DEPTH_LIMIT", 50)
settings.set("ITEM_PIPELINES", {'upwork.pipelines.SavePipeline': 300})
settings.set('DOWNLOAD_DELAY', 1)
settings.set("MONGO_URI", '')
settings.set("MONGO_DATABASE", 'test')
crawler = Crawler(JobSpider,settings)

crawler.signals.connect(spider_closing, signal=signals.spider_closed)

crawler.crawl(JobSpider())
reactor.run()