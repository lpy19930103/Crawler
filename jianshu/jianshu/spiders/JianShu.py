import scrapy

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
}


class JianShuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    domain = 'http://jianshu.com'
    base_url = 'https://www.jianshu.com/search?q=python%E7%88%AC%E8%99%AB&page='

    num = 0

    def start_requests(self):
        while self.num < 2:
            self.num += 1
            yield scrapy.Request(self.base_url + str(self.num) + "&type=note",
                                 headers=headers, callback=self.parse)

    def parse(self, response):
        title = response.xpath('//title/text()').extract()
        link = response.xpath('//div[@class="meta"]/a/@href').extract()
        print(link)
        print(title)
