import scrapy

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
}

cookies = 'q_c1=39373d3162a94dabbc7765129a82886f|1506651578000|1506651578000; _zap=40662f1c-8873-4598-9360-ff96f8a09ca4; d_c0="AEBCWzg6cwyPTmJB1r2tgXE_srnzGz88AEo=|1506671211"; _ga=GA1.2.1091259282.1506671212; q_c1=39373d3162a94dabbc7765129a82886f|1514858506000|1506651578000; __utmz=155987696.1516091837.1.1.utmcsr=dongwm.com|utmccn=(referral)|utmcmd=referral|utmcct=/archives/%E6%88%91%E7%9A%84%E7%9F%A5%E4%B9%8ELive/; __utma=155987696.1091259282.1506671212.1516091837.1516356956.2; aliyungf_tc=AQAAAN9iZh2DJgcATwLNcwK5DKpmz3Zi; _xsrf=f9841ea1-876e-4a0c-a343-0c835da3fa38; capsion_ticket="2|1:0|10:1516598928|14:capsion_ticket|44:YjcyYjFlNGRhMDcyNDM4ODk1OTQzMDUyMGY5MjI3MjY=|946c5583f91e4861354d6e2e6cc6cf6812b5ceb5d65a9d35ffe30fe2269c752e"; z_c0="2|1:0|10:1516599008|4:z_c0|92:Mi4xUEV5NUFnQUFBQUFBUUVKYk9EcHpEQ1lBQUFCZ0FsVk40TVJTV3dBbDc4OTB6RE5jRGNJY214RGlvRDlqWFlPLU9R|42f7839a2a25ac5fabf2b29b48e651e949e6b96b218b0fb51257bcfbc4236235"'


class DownloadSpiders(scrapy.Spider):
    name = "download"
    allowed_domains = ["https://www.zhihu.com/"]
    start_urls = [
        "https://www.zhihu.com/",
    ]

    def start_requests(self):
        yield scrapy.Request("https://www.zhihu.com/",
                             headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):
        imgs = response.xpath('//meta[@itemprop="image"]/@content').extract()
        print(imgs)
