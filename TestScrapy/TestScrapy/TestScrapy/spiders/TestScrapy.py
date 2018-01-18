import scrapy
import ssl

from scrapy import Request

ssl._create_default_https_context = ssl._create_unverified_context
from fake_useragent import UserAgent

ua = UserAgent();


class TestScrapy(scrapy.Spider):
    name = 'TestScrapy'
    start_urls = ['https://www.jianshu.com/p/9907c2f8f4c2']

    def start_requests(self):
        yield Request("https://www.jianshu.com/p/9907c2f8f4c2",
                      headers={'User-Agent': ua.random})

    def parse(self, response):
        item = TestscrapyItem()
        item['title'] = response.xpath('//h1[@class = "title"]/text()').extract()
        item['author'] = response.xpath('//div[@class = "info"]/span[@class = "name"]/a/text()').extract()
        item['contents'] = response.xpath('//div[@class = "show-content"]/p/text()').extract()
        print(item)
        yield item
        # title = response.xpath('//h1[@class = "title"]/text()').extract()
        # author = response.xpath('//div[@class = "info"]/span[@class = "name"]/a/text()').extract()
        # contents = response.xpath('//div[@class = "show-content"]/p/text()').extract()
        # for content in contents:
        #     print(content)
        #
        # print("title = ", title)
        # print("author = ", author)
        # print(content)


class TestscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    contents = scrapy.Field()
