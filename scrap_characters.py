import scrapy

class BlogSpider(scrapy.Spider):
    name = 'charactersspider'
    start_urls = ['https://fr.wikipedia.org/wiki/Catégorie:Personnage_d%27animation']

    def parse(self, response):
        for character in response.css('div#mw-pages div.mw-content-ltr div.mw-category div.mw-category-group ul li a'):
            yield {'character': character.css('a ::text').get()}
