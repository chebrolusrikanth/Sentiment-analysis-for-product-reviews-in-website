import scrapy

class Extract_tabledata(scrapy.Spider):
    name='Table_data'

    start_urls=['https://en.wikipedia.org/wiki/World_population']

    def parse(self, response):
        head=response.css('.wikitable:nth-child(15) th::text').extract()
        yield{
            'Header1':head[0],
            'Header2':head[1],
            'Header3':head[2]
        }

        for col in  response.css('.wikitable:nth-child(15) td::text').extract():
            yield{
                'column1':col[0],
                'column2':col[1],
                'column3':col[2],
            }