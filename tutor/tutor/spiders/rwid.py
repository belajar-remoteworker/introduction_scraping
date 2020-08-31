import scrapy


class RwidSpider(scrapy.Spider):
    name = 'rwid'
    allowed_domains = ['167.172.70.208:9999']

    #mulai dari url ini
    start_urls = ['http://167.172.70.208:9999/']

    def parse(self, response):
        yield {'title': response.css('title:text').get()}

        #pass
