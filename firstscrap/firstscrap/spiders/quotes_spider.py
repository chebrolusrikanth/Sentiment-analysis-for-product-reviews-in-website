import scrapy

class QuotesSpider(scrapy.Spider):
    name='quotes'

    start_urls=["https://www.flipkart.com/search?sid=bks&otracker=CLP_Filters&p%5B%5D=facets.language%255B%255D%3DEnglish"]

    def parse(self, response):
        word=response.css('div.Nx9bqj::text').extract()
        yield{
            "word":word
        }