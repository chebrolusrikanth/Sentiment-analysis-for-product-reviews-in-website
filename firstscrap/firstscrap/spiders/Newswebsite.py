import scrapy

class News(scrapy.Spider):
    name='Newspaper'

    start_urls=['https://timesofindia.indiatimes.com/news']

    def parse(self, response):

        yield{
            'Head_lines':response.css('p.CRKrj::text').extract(),
            'Links':response.css('a::attr(href)').extract() 
        }