import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from fake_useragent import UserAgent

ua = UserAgent();


class MyImageSpider(scrapy.Spider):
    name = 'image_spider'
    allowed_domains = ["https://www.jianshu.com/p/9907c2f8f4c2"]
    start_urls = [
        "https://www.jianshu.com/p/9907c2f8f4c2",
    ]

    def start_requests(self):
        yield Request("https://www.jianshu.com/p/9907c2f8f4c2",
                      headers={'User-Agent': ua.random})

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        imgs = hxs.select('//img/@data-original-src').re(r'//\s*(.*)')
        img_paths = []
        for img in imgs:
            img_paths.append("https://" + img)
        item = PicItem()
        item['image_urls'] = img_paths
        print('item = ', item)
        return item


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item


class PicItem(scrapy.Item):
    # ... other item fields ...
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()
