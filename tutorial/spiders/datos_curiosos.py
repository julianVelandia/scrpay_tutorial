import scrapy

class DatosCuriosos(scrapy.Spider):
    name = 'datos'
    start_urls = [
        'https://mott.pe/noticias/datos-curiosos-que-te-despertaran-las-ganas-por-aprender-mas/'
    ]

    def parse(self, response):
        titles = response.xpath('//div[@class="text"]//h2//text()').getall()
        
        yield {
            'title': titles
        }
        

        
        
       