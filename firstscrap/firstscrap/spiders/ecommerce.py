import scrapy
class ecom(scrapy.Spider):
    name='ecommerce'

    start_urls=['https://www.flipkart.com/search?sid=bks&otracker=CLP_Filters&p%5B%5D=facets.language%255B%255D%3DEnglish']

    def parse(self,response):
        book=response.css('a.wjcEIp::text').extract()
        price=response.css('div.Nx9bqj::text').extract()
        rate=response.css('div.XQDdHH::text').extract()
        if response.css('div.XQDdHH::text').extract() == None:
            rate='No rateing'
        yield{
        "Book_name":book,
        "Price":price,
        "Rating":rate,           
        } 