import scrapy

class BlogSpider(scrapy.Spider):
    name = 'quotesspider'
    start_urls = ['https://www.babelio.com/auteur/Frederic-Dard/7187/citations']

    def parse(self, response):
        for quote in response.css('div.post_con div.text.row > div'):
            yield {'quote': (quote.css('div ::text').extract_first()).strip()}

        next_page_href = response.css('div.pagination.row > a.active + a::attr(href)').get()
        if next_page_href is not None:
            next_page = response.urljoin(next_page_href)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)