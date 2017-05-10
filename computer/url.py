import scrapy
#from scrapy.spider import Spider
#import bs4

class BlogSpider(spider.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('h2.entry-title'):
            yield {'title': title.css('a ::text').extract_first()}

        next_page = response.css('div.prev-post > a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

#class Newsscrapy(scrapy.Scrapy):
    #name = 'newsscrapy'
    #start_url = ["http://www.appledaily.com.tw/"]

    #def parse(self, response):
        #for title in response.class:
            #pass NotImplementedError