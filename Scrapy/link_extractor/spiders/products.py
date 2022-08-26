from gc import callbacks
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ProductsSpider(CrawlSpider):
    name = 'products'
    allowed_domains = ['sparkfun.com']
    start_urls = ['http://sparkfun.com/categories']

    rules = [
        Rule(
            LinkExtractor(
              restrict_text=(r"(?P<name>Cable)")  
            )
        ),
        Rule(
            LinkExtractor(
                allow=(r"page=\d",)
            ), callback="parse_page"
        )
    ]

    def parse_page(self, response):
        items = response.css('div.tile')
        for item in items:

            yield {
                "name": item.css("h3.title span::text").get(),
                "sku": item.css("span.sku::text").get().replace("\n", "").strip(),
                "price": item.css("span.price::text").get(),
            }
