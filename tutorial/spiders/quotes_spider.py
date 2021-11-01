import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        '''
        with open('resultados.txt', 'w', encoding='utf-8') as f:
            f.write(quotes.text)
        '''

        yield {
            'quotes' : quotes
        }
        
        
       