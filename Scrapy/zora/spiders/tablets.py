import scrapy


class TabletSpider(scrapy.Spider):
    name = 'tablets'
    allowed_domains = ['www.zora.bg']
    start_urls = ['https://zora.bg/category/tableti2?operacionna-sistema-1=ios-5']


    
    def parse(self, response):
        products = response.css('div._product-inner')
        for product in products:
            yield {
                'name': product.css('div._product-inner a::attr(title)').get(),
                'price': product.css('div._product-price::text').get(),
                'delivery': product.css('span::text').get(),
                
            }