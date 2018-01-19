import scrapy

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
}


class DownloadSpiders(scrapy.Spider):
    name = "download"
    allowed_domains = ["https://www.zhihu.com/"]
    start_urls = [
        "https://www.zhihu.com/",
    ]

    def start_requests(self):
            yield scrapy.Request( "https://www.zhihu.com/",
                headers=headers, callback=self.parse)

    def parse(self, response):
        imgs = response.xpath('//meta[@itemprop="image"]/@content').extract()
        print(imgs)
